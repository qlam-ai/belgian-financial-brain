# belgian-financial-brain
LLM fuelled by data about the Belgian Stock Market
Here’s a polished and professional README for your GitHub repository:

---

# Belgian Financial Brain

[![Stars](https://img.shields.io/github/stars/qlam-ai/belgian-financial-brain?style=social)](https://github.com/qlam-ai/belgian-financial-brain/stargazers)  
[![Issues](https://img.shields.io/github/issues/qlam-ai/belgian-financial-brain)](https://github.com/qlam-ai/belgian-financial-brain/issues)  
[![License](https://img.shields.io/github/license/qlam-ai/belgian-financial-brain)](LICENSE)

**Belgian Financial Brain** combines the power of live stock market data with the intelligence of locally hosted LLMs. This project fetches real-time financial data for the top 20 Belgian stocks and ETFs and integrates it seamlessly with the `llama-3.2-3B-Instruct-4bit` model (optimized for MLX usage). This integration empowers your local LLMs with access to live and precise financial information, enabling advanced decision-making and conversational capabilities.

---

## 🚀 Features

- **Real-Time Stock Data Fetching**:  
  Automatically retrieves and updates data for the top 20 Belgian stocks and ETFs.
  
- **LLM Integration**:  
  Uses `llama-3.2-3B-Instruct-4bit` to process, analyze, and answer questions about financial data in natural language.

- **Dynamic and Local**:  
  Brings the power of live financial updates to locally hosted AI models, ensuring privacy and independence from cloud-based APIs.

- **Custom Queries**:  
  Ask specific questions about stock trends, performance, or financial indicators and get contextually relevant answers.

---

## 🛠️ Installation & Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/qlam-ai/belgian-financial-brain.git
   cd belgian-financial-brain
   ```

2. **Install Dependencies**:  
   Ensure you have Python 3.8+ installed, then install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```
   
3. **Run the Application**:
   Fetch live stock data and enable LLM-powered queries:
   ```bash
   python main_chat.py
   ```

---

## 🧠 How It Works

1. **Fetch Financial Data**:  
   The script collects up-to-date information about Belgian stocks and ETFs using APIs and/or scraping methods.

2. **Feed Data into the LLM**:  
   The live data is formatted and fed into `llama-3.2-3B-Instruct-4bit`.

3. **Ask Financial Questions**:  
   Interact with the LLM to ask targeted financial queries. Examples:
   - "What is the performance trend for company X over the last week?"
   - "Which Belgian ETFs are showing positive growth today?"

---

## 🗂️ Repository Structure

```plaintext
belgian-financial-brain/
├── data/              # Scripts and modules for fetching financial data
├── models/            # Scripts for LLM integration and query handling
├── tests/             # Unit tests for data fetching and LLM integration
├── requirements.txt   # Required Python libraries
├── main.py            # Main application script
├── README.md          # Project documentation
└── LICENSE            # License file
```

---

## 🔧 Customization

- **Add More Stocks/ETFs**:  
  Update the stock list in `data/fetch_stocks.py` to include additional Belgian financial instruments.

- **Optimize Model Performance**:  
  Experiment with `llama-3.2-3B-Instruct-4bit` configuration or substitute it with other LLMs compatible with MLX for different requirements.

---

## 📈 Future Plans

- Add support for additional European markets.  
- Integrate more advanced financial metrics and visualizations.  
- Build a web-based or CLI interface for easier usage.  

---

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 💬 Questions or Suggestions?

Feel free to open an [issue](https://github.com/qlam-ai/belgian-financial-brain/issues) or submit a pull request. Contributions are welcome!

---

### ⭐ If you find this project useful, don’t forget to give it a star!  

--- 

Let me know if you'd like additional sections, such as installation specifics for the MLX model or deeper technical details!