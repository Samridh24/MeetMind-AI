
# MeetMind AI 🧠

An AI-powered meeting analysis assistant that helps users understand meeting discussions, generate summaries, and ask questions about meeting content using **Retrieval-Augmented Generation (RAG)**.

## 🚀 Features

- 🎙️ Upload meeting audio for analysis
- 📝 Generate AI-powered meeting summaries
- 📌 Extract key conclusions and discussion points
- 👥 Identify assigned tasks and responsibilities
- 📅 Retrieve meeting dates and follow-up details
- 💬 Ask questions about meeting content using RAG
- 🗂️ Store and manage multiple meeting reports
- 🌓 Interactive Streamlit user interface
- 🗄️ SQLite database integration

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | User interface |
| Google Gemini API | AI-powered meeting analysis |
| ChromaDB | Vector storage for RAG |
| SQLite | Meeting data storage |
| Python-dotenv | Environment variable management |

## 📁 Project Structure

```text
MeetMind-AI/
│
├── app.py                 # Main Streamlit application
├── gemini_service.py      # Gemini API integration
├── rag_service.py         # RAG and question answering
├── database_service.py    # SQLite database operations
├── requirements.txt       # Project dependencies
├── .gitignore             # Ignored files and secrets
│
├── test_database.py       # Database testing
├── test_gemini.py         # Gemini service testing
└── test_rag.py            # RAG service testing
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Samridh24/MeetMind-AI.git
cd MeetMind-AI
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment on Windows:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the API Key

Create a `.env` file in the project root directory:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

Replace the placeholder with your own Google Gemini API key.

> **Security Note:** Never upload your `.env` file or expose your API key publicly.

### 5. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

## 🔄 Application Workflow

1. Upload a meeting audio file.
2. Process and analyze the meeting using the Gemini API.
3. Generate a structured meeting report.
4. Store the report in the SQLite database.
5. Index meeting information for retrieval.
6. Ask questions about the meeting using the RAG system.
7. Retrieve relevant information and generate an answer.

## 🧩 Core Modules

### `app.py`

Provides the Streamlit interface and connects the application's different services.

### `gemini_service.py`

Handles communication with the Google Gemini API and meeting analysis.

### `database_service.py`

Manages SQLite database operations, including saving, retrieving, and deleting meetings.

### `rag_service.py`

Stores meeting reports and retrieves relevant information to answer user questions using RAG.

## 🧪 Testing

The project includes test files for the main services:

```bash
python test_database.py
python test_gemini.py
python test_rag.py
```

Ensure that all dependencies and environment variables are configured before running API-related tests.

## 🔮 Future Enhancements

- Speaker identification and diarization
- Automatic action-item tracking
- Calendar integration
- Export reports as PDF or DOCX
- User authentication
- Cloud database integration
- Multilingual meeting support

## 👨‍💻 Author

**Samridh Sagar**

GitHub: [Samridh24](https://github.com/Samridh24)

## 📄 License

This project is intended for educational and portfolio purposes.
