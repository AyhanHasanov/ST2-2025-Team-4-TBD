# LLM Budget Advisor Microservice

A FastAPI-based microservice that leverages a locally running Ollama model (Qwen3:8b) to provide expense analysis and budgeting advice.

## 🚀 Features

- **Expense Summarization**: Analyze spending patterns and get natural-language insights
- **Budgeting Advice**: Ask questions and receive practical budgeting tips
- **Local LLM**: Uses Ollama for privacy-focused, offline AI processing
- **Clean API**: RESTful endpoints with JSON responses
- **Error Handling**: Comprehensive error handling and logging

## 📋 Prerequisites

- Python 3.10 or higher
- [Ollama](https://ollama.ai/) installed and running locally
- Qwen3:8b model pulled in Ollama

## 🔧 Installation

### 1. Install Dependencies

Navigate to the project directory and install required packages:

```bash
cd llm_service
pip install -r requirements.txt
```

### 2. Install and Setup Ollama

#### Install Ollama:
- Download from [ollama.ai](https://ollama.ai/)
- Follow installation instructions for your OS

#### Pull the Qwen3:8b Model:
```bash
ollama pull qwen2.5:3b
```

#### Verify Ollama is Running:
```bash
ollama list
```

You should see `qwen2.5:3b` in the list.

## ▶️ Running the Service

### Start the FastAPI server:

```bash
uvicorn main:app --reload --port 8000
```

Or run directly with Python:

```bash
python main.py
```

The service will be available at:
- API: http://localhost:8000
- Interactive Docs: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 📡 API Endpoints

### 1. Health Check

```http
GET /
GET /health
```

Returns service status and available endpoints.

### 2. Expense Summarization

```http
POST /api/summarize
Content-Type: application/json
```

**Request Body:**
```json
{
  "expenses": [
    {"category": "Food", "amount": 45.50},
    {"category": "Transport", "amount": 20.00},
    {"category": "Entertainment", "amount": 35.00},
    {"category": "Food", "amount": 28.75}
  ]
}
```

**Response:**
```json
{
  "summary": "Your spending shows a focus on food ($74.25) and entertainment. Consider meal planning to reduce food costs and set entertainment limits.",
  "total_amount": 129.25,
  "expense_count": 4
}
```

### 3. Budgeting Advice

```http
POST /api/advice
Content-Type: application/json
```

**Request Body:**
```json
{
  "question": "How can I reduce my monthly grocery expenses?"
}
```

**Response:**
```json
{
  "advice": "Create a weekly meal plan and shopping list before going to the store. Buy generic brands and shop seasonal produce to save 20-30% on groceries without sacrificing nutrition.",
  "question": "How can I reduce my monthly grocery expenses?"
}
```

## 🧪 Testing with Postman

### Import Collection:

1. Open Postman
2. Create a new request collection
3. Add the endpoints above

### Test Expense Summarization:

1. Create a new POST request to `http://localhost:8000/api/summarize`
2. Set Headers: `Content-Type: application/json`
3. Set Body (raw JSON):
```json
{
  "expenses": [
    {"category": "Groceries", "amount": 150.00},
    {"category": "Gas", "amount": 60.00},
    {"category": "Dining Out", "amount": 85.50}
  ]
}
```
4. Click Send

### Test Budgeting Advice:

1. Create a new POST request to `http://localhost:8000/api/advice`
2. Set Headers: `Content-Type: application/json`
3. Set Body (raw JSON):
```json
{
  "question": "What's the best way to start an emergency fund?"
}
```
4. Click Send

## 🧰 Testing with cURL

### Summarize Expenses:
```bash
curl -X POST http://localhost:8000/api/summarize \
  -H "Content-Type: application/json" \
  -d '{
    "expenses": [
      {"category": "Food", "amount": 45.50},
      {"category": "Transport", "amount": 20.00}
    ]
  }'
```

### Get Advice:
```bash
curl -X POST http://localhost:8000/api/advice \
  -H "Content-Type: application/json" \
  -d '{
    "question": "How can I save money on utilities?"
  }'
```

## 📁 Project Structure

```
llm_service/
├── main.py              # FastAPI app initialization and router registration
├── requirements.txt     # Python dependencies
├── routes/
│   ├── summarize.py    # Expense summarization endpoint
│   └── advice.py       # Budgeting advice endpoint
├── utils/
│   └── prompts.py      # LLM prompt templates
└── README.md           # This file
```

## 🔍 Troubleshooting

### Ollama Connection Error (503)
- Ensure Ollama is running: `ollama serve`
- Check if accessible: `curl http://localhost:11434/api/tags`

### Model Not Found Error
- Pull the model: `ollama pull qwen2.5:3b`
- Verify: `ollama list`

### Timeout Errors
- The model may be loading for the first time (takes longer)
- Increase timeout in route files if needed
- Check system resources (RAM, CPU)

### Import Errors
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Verify Python version: `python --version` (should be 3.10+)

## 📝 Notes

- First request to each endpoint may take longer as the model loads
- Responses are generated by the local LLM and may vary
- No data is sent to external services - everything runs locally
- Logging is enabled for debugging and monitoring

## 🔒 Security Considerations

- This service is designed for local development
- For production deployment:
  - Configure specific CORS origins
  - Add authentication and rate limiting
  - Use environment variables for configuration
  - Implement input validation and sanitization

## 📄 License

This project is provided as-is for educational and development purposes.

## 🤝 Contributing

Feel free to extend this service with additional endpoints or features:
- Budget goal tracking
- Spending trend analysis
- Category-specific insights
- Multi-language support

---

**Happy Budgeting! 💰**


