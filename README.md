# 🧠 POC: AI-Powered Browser Automation & Testing

## 🚀 Project Objective
This project integrates an **AI-powered test agent** with **browser automation** to facilitate intelligent UI testing. It leverages **Google Gemini AI** for interpreting and validating test results and uses **Browser Use** libraries for browser automation and control.

### **Key Goals:**
- Automate test execution using AI-powered strategies.
- Implement self-healing tests to adapt to UI changes.
- Generate AI-based test insights and reports.

---

## 📁 Project Structure
```
AutomationTestingAgent/
│── .gitignore               # Ignored files (e.g., .env)
│── agentAI.py               # AI-driven automation script
│── agent_history.gif        # Sample test execution result
│── agentresults.json        # Stored test results
│── README.md                # Project documentation
│── .idea/                   # PyCharm settings (not required in Git)
└── .env                     # Environment variables (ignored)
```

---

## **Key Components**

### **1. AI Engine (Google Gemini + LangChain)**

- **Library Used:** `langchain_google_genai`
- **Model Used:** `gemini-2.0-flash-exp`
- **Purpose:**
  - The script initializes a **ChatGoogleGenerativeAI** model from **LangChain**.
  - The AI agent (`Agent` class) interprets and executes test steps.
  - It processes the test flow and validates the extracted results.
  - The AI-generated results are stored in a JSON file (`agentresults.json`).
  - The final test results are structured and validated using **Pydantic** (`CheckoutResult` model).

- **Integration Flow:**
  1. The `Agent` receives a structured test task.
  2. It uses **Gemini AI** to interpret and execute the instructions.
  3. The AI processes the browser's extracted data and validates it against expectations.
  4. The final structured response is stored and validated.

---

### **2. Browser Automation (Browser Use Library)**

- **Libraries Used:**
  - `browser_use.agent.views` → `ActionResult`
  - `browser_use.browser.context` → `BrowserContext`
  - `browser_use.controller.service` → `Controller`
  - `browser_use.agent.service` → `Agent`

- **Purpose:**
  - Handles **browser automation** through an agent-based approach.
  - `BrowserContext` provides an interface for interacting with the browser.
  - `Controller` is responsible for defining test actions and structuring results.
  - `Agent` executes actions in the browser under AI guidance.

- **Key Function:**
  - **`get_attr_URL(browser: BrowserContext)`**
    - Extracts **current URL** and **an element's attribute** using the browser context.
    - Demonstrates how the **AI-driven agent** can interact with the browser and retrieve data dynamically.

---

## 💡 How to Use
### **Prerequisites**
- Install dependencies using:
  ```bash
  pip install -r requirements.txt
  ```
- Ensure you have a **Google Gemini API Key** stored in a `.env` file:
  ```env
  GEMINI_API_KEY=your_api_key_here
  ```

### **Run the Script**
```bash
python agentAI.py
```


---

## 📌 Future Enhancements
- Add AI-driven locators for robust element detection.
- Implement Healenium for auto-correcting test failures.
- Improve result visualization and test analytics.
  
---
## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## **Contact**
For any inquiries, feel free to reach out!

