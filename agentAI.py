import asyncio
import os
import json

from browser_use.agent.views import ActionResult
from browser_use.browser.context import BrowserContext
from browser_use.controller.service import Controller
from dotenv import load_dotenv
from browser_use.agent.service import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import SecretStr, BaseModel

# Load API key from .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
class CheckoutResult(BaseModel):
    login_status: str
    cart_status: str
    checkout_status: str
    total_update_status: str
    delivery_location_status: str
    confirmation_message: str

controller = Controller(output_model=CheckoutResult)


# @controller.action('Open Base Websit')
# async def open_website(browser : BrowserContext):
#     page = await  browser.get_current_page()
#     await page.goto('https://rahulshettyacademy.com/loginpagePractise/')
#     return ActionResult(extracted_content = 'Browser has been opened')

@controller.action('Get Attribute and URL of the page')
async def get_attr_URL(browser : BrowserContext):
    page = await browser.get_current_page()
    current_url = page.url
    attr = await page.get_by_text("Shop Name").get_attribute('class')
    print(current_url)
    return ActionResult(extracted_content='Current URL is {current_url} and attribute is {attr}')




async def SiteValidation():
    if not api_key:
        raise ValueError("GEMINI_API_KEY is not set. Please check your .env file.")

    task = (
        "Important: I am a UI Automation tester validating the tasks. "
        "1. Open browser and navigate to https://rahulshettyacademy.com/loginpagePractise/ "
        "2. Log in using credentials found on the page. "
        "3. Get Attribute and URL of the page"
        "4. Select the first 2 products and add them to the cart. "
        "5. Check out and store the total value displayed on screen. "
        "6. Increase the quantity of any product and verify the total updates accordingly. "
        "7. Complete checkout, select country, agree to terms, and purchase. "
        "8. Verify that a 'Thank You' message is displayed."
    )

    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp", api_key=SecretStr(api_key))
    agent = Agent(task=task, llm=llm, controller=controller, use_vision=True)

    history = await agent.run()
    history.save_to_file('agentresults.json')

    test_results = history.final_result()

    if not test_results:
        raise ValueError("Agent failed to return valid test results.")

    # ✅ Convert JSON string to dictionary
    if isinstance(test_results, str):
        test_results = json.loads(test_results)

    # ✅ Pass the dictionary to model_validate()
    validated_result = CheckoutResult.model_validate(test_results)

    assert validated_result.confirmation_message == "Thank you! Your order will be delivered in next few weeks :-)."

# Run the async function properly
if __name__ == "__main__":
    asyncio.run(SiteValidation())
