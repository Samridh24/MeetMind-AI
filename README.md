
# 🧠 MeetMind AI

### AI-Powered Meeting Analysis & Intelligent Q&A Assistant

MeetMind AI is an AI-powered meeting analysis application that helps users extract meaningful insights from meeting audio. The application uses the **Google Gemini API** to analyze meeting discussions, generate structured summaries, identify important conclusions, and retrieve relevant information through a **Retrieval-Augmented Generation (RAG)** pipeline.

The project is designed to make meeting management more efficient by allowing users to upload meeting recordings, access organized meeting reports, and ask natural-language questions about meeting content.

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Problem Statement](#-problem-statement)
- [Project Objectives](#-project-objectives)
- [Key Features](#-key-features)
- [How It Works](#-how-it-works)
- [System Architecture](#-system-architecture)
- [Technology Stack](#-technology-stack)
- [Project Structure](#-project-structure)
- [Installation and Setup](#-installation-and-setup)
- [Environment Configuration](#-environment-configuration)
- [Running the Application](#-running-the-application)
- [Core Modules](#-core-modules)
- [RAG-Based Question Answering](#-rag-based-question-answering)
- [Database Management](#-database-management)
- [Testing](#-testing)
- [Example Use Cases](#-example-use-cases)
- [Limitations](#-limitations)
- [Future Enhancements](#-future-enhancements)
- [Learning Outcomes](#-learning-outcomes)
- [Author](#-author)

---

## 🚀 Overview

MeetMind AI combines generative AI, audio analysis, database management, and Retrieval-Augmented Generation to create an intelligent meeting assistant.

Instead of manually reviewing an entire meeting recording, users can use the application to:

- Understand the main topics discussed.
- Generate a structured meeting summary.
- Identify decisions and important conclusions.
- Review assigned tasks and responsibilities.
- Retrieve information from previously analyzed meetings.
- Ask questions about meeting discussions.
- Manage multiple meeting reports.

The application uses a Streamlit interface, making it easy to interact with the system through a web browser.

---

## ❓ Problem Statement

Meetings often contain large amounts of information, including discussions, decisions, deadlines, and assigned responsibilities.

Manually reviewing meeting recordings can be time-consuming and important details may be missed.

MeetMind AI aims to address this problem by providing an intelligent system that can analyze meeting audio, organize the information, and allow users to retrieve relevant details through natural-language questions.

---

## 🎯 Project Objectives

The main objectives of MeetMind AI are:

1. Develop an AI-based system for analyzing meeting recordings.
2. Generate meaningful and structured meeting summaries.
3. Extract important discussion points and conclusions.
4. Store meeting information for future reference.
5. Implement RAG-based question answering.
6. Provide a simple and interactive user interface.
7. Demonstrate the practical use of Generative AI and vector-based retrieval.
8. Build a modular application with separate AI, database, and retrieval services.

---

## ✨ Key Features

### 🎙️ 1. Meeting Audio Analysis

Users can upload meeting audio through the Streamlit interface.

The application sends the audio for AI-powered analysis and generates a structured report containing relevant meeting information.

### 📝 2. AI-Generated Meeting Summaries

The system generates summaries to help users quickly understand the meeting without reviewing the complete recording.

The generated report may include:

- Meeting overview.
- Main discussion points.
- Important conclusions.
- Decisions taken during the meeting.
- Follow-up information.

### 📌 3. Important Information Extraction

MeetMind AI is designed to identify useful information from meeting discussions, such as:

- Key decisions.
- Important conclusions.
- Work assignments.
- Responsibilities.
- Deadlines and dates mentioned in the discussion.

The accuracy of extracted information depends on the quality of the audio and the AI-generated analysis.

### 💬 4. RAG-Based Question Answering

Users can ask questions about analyzed meeting reports using natural language.

Example questions:

- What were the main conclusions of the meeting?
- What tasks were assigned?
- What deadline was discussed?
- What should be completed before the next meeting?
- What decisions were made?

The RAG pipeline retrieves relevant meeting information and uses it to generate an answer.

### 🗂️ 5. Multiple Meeting Management

The application includes database functionality to store and manage meeting reports.

Users can work with multiple meeting records instead of limiting the application to a single meeting.

### 🗄️ 6. SQLite Database Integration

SQLite is used to store meeting-related information locally.

The database service supports operations such as:

- Saving meeting records.
- Retrieving meeting records.
- Fetching individual meetings.
- Deleting meeting records.

### 🖥️ 7. Interactive Streamlit Interface

The application uses Streamlit to provide a simple interface for:

- Uploading meeting audio.
- Viewing meeting analysis.
- Accessing stored meetings.
- Asking questions.
- Reviewing generated reports.

### 🔐 8. Environment Variable Configuration

The Gemini API key is stored using environment variables rather than being directly written into the application code.

This helps prevent accidental exposure of API credentials.

---

## 🔄 How It Works

The overall application workflow is:

```text
                ┌─────────────────────────┐
                │     User Uploads Audio  │
                └────────────┬────────────┘
                             │
                             ▼
                ┌─────────────────────────┐
                │   Streamlit Interface   │
                └────────────┬────────────┘
                             │
                             ▼
                ┌─────────────────────────┐
                │   Gemini AI Analysis    │
                └────────────┬────────────┘
                             │
                             ▼
                ┌─────────────────────────┐
                │ Structured Meeting Report│
                └────────────┬────────────┘
                             │
                 ┌───────────┴───────────┐
                 ▼                       ▼
      ┌──────────────────┐    ┌──────────────────┐
      │  SQLite Database │    │  RAG / ChromaDB  │
      └────────┬─────────┘    └────────┬─────────┘
               │                       │
               └───────────┬───────────┘
                           ▼
                ┌─────────────────────────┐
                │ User Asks a Question    │
                └────────────┬────────────┘
                             │
                             ▼
                ┌─────────────────────────┐
                │ Retrieve Relevant Data  │
                └────────────┬────────────┘
                             │
                             ▼
                ┌─────────────────────────┐
                │ Generate AI-Based Answer│
                └─────────────────────────┘
```

---

## 🏗️ System Architecture

MeetMind AI follows a modular service-based structure.

### 1. Presentation Layer

The Streamlit application acts as the presentation layer.

It allows users to interact with the system through an accessible web interface.

### 2. AI Analysis Layer

The Gemini service handles communication with the Google Gemini API.

It is responsible for processing meeting audio and generating an analysis.

### 3. Data Storage Layer

The database service manages the SQLite database.

Meeting records can be stored and retrieved for future access.

### 4. Retrieval Layer

The RAG service stores meeting report information and retrieves relevant content when users ask questions.

ChromaDB is used as the vector storage component for retrieval functionality.

### 5. Question Answering Layer

The retrieved information is used to support answers to user questions about meeting reports.

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Streamlit | Web-based user interface |
| Google Gemini API | AI-powered meeting analysis |
| ChromaDB | Vector storage and retrieval |
| SQLite | Local meeting data storage |
| Python-dotenv | Environment variable management |
| Git & GitHub | Version control and project hosting |

---

## 📁 Project Structure

```text
MeetMind-AI/
│
├── app.py
│   └── Main Streamlit application
│
├── gemini_service.py
│   └── Gemini API integration and meeting analysis
│
├── rag_service.py
│   └── RAG functionality and question answering
│
├── database_service.py
│   └── SQLite database operations
│
├── requirements.txt
│   └── Project dependencies
│
├── .gitignore
│   └── Ignored files, local databases, and secrets
│
├── test_database.py
│   └── Database testing
│
├── test_gemini.py
│   └── Gemini service testing
│
└── test_rag.py
    └── RAG service testing
```

---

## ⚙️ Installation and Setup

### Step 1: Clone the Repository

Open a terminal and run:

```bash
git clone https://github.com/Samridh24/MeetMind-AI.git
```

Move into the project directory:

```bash
cd MeetMind-AI
```

---

### Step 2: Create a Virtual Environment

Create a Python virtual environment:

```bash
python -m venv venv
```

Activate the environment on Windows:

```bash
venv\Scripts\activate
```

For macOS or Linux:

```bash
source venv/bin/activate
```

---

### Step 3: Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Configuration

MeetMind AI requires a Google Gemini API key.

Create a file named `.env` in the root directory of the project.

Add the following:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

Replace the placeholder with your own API key.

### Security Guidelines

- Do not commit the `.env` file to GitHub.
- Do not share your API key publicly.
- Do not hardcode API credentials in Python files.
- Use environment variables for sensitive configuration.
- Regenerate the API key if it is accidentally exposed.

---

## ▶️ Running the Application

After activating the virtual environment and installing dependencies, run:

```bash
streamlit run app.py
```

The application will start locally and provide a URL that can be opened in a web browser.

---

## 🧩 Core Modules

### 📄 `app.py`

The main application file.

Responsibilities include:

- Displaying the Streamlit interface.
- Accepting user input.
- Handling meeting-related interactions.
- Connecting the AI analysis, database, and RAG services.
- Displaying meeting reports and answers.

### 🤖 `gemini_service.py`

This module handles integration with the Google Gemini API.

Responsibilities include:

- Accessing the API key from environment variables.
- Sending meeting audio for analysis.
- Generating AI-based meeting reports.
- Returning analysis results to the application.

### 🗄️ `database_service.py`

This module manages SQLite database operations.

Responsibilities include:

- Initializing the database.
- Saving meeting records.
- Retrieving all meetings.
- Fetching individual meeting details.
- Deleting meeting records.

### 🔍 `rag_service.py`

This module handles the retrieval functionality.

Responsibilities include:

- Storing meeting reports for retrieval.
- Connecting meeting information with the retrieval system.
- Finding relevant content for user questions.
- Supporting question answering based on stored meeting reports.

---

## 🧠 RAG-Based Question Answering

Retrieval-Augmented Generation, commonly known as RAG, combines information retrieval with generative AI.

Instead of relying only on the model's general knowledge, the system retrieves relevant information from stored content and uses that information to support its response.

### RAG Workflow in MeetMind AI

```text
Meeting Report
      │
      ▼
Text Preparation
      │
      ▼
Document Storage
      │
      ▼
Vector Representation
      │
      ▼
ChromaDB Storage
      │
      ▼
User Question
      │
      ▼
Relevant Information Retrieval
      │
      ▼
AI-Generated Response
```

### Benefits of Using RAG

- Helps retrieve information from stored meeting reports.
- Supports questions about specific meeting content.
- Reduces the need to manually search through reports.
- Makes the application more useful for repeated meeting references.
- Demonstrates the practical implementation of an AI retrieval pipeline.

The quality of the response depends on the quality of the stored reports, retrieval process, and AI-generated output.

---

## 🗃️ Database Management

MeetMind AI uses SQLite for local data storage.

The database layer is designed to manage meeting records and provide persistent access to saved meeting information.

### Database Operations

The application supports operations such as:

- Database initialization.
- Saving meeting reports.
- Retrieving all stored meetings.
- Fetching a particular meeting.
- Deleting meeting records.

SQLite is suitable for this project because it is lightweight, easy to configure, and does not require a separate database server for local development.

---

## 🧪 Testing

The repository contains test files for different application services.

### Run Database Tests

```bash
python test_database.py
```

### Run Gemini Service Tests

```bash
python test_gemini.py
```

### Run RAG Tests

```bash
python test_rag.py
```

Before running tests, ensure that:

- The virtual environment is activated.
- Required dependencies are installed.
- Environment variables are configured where required.
- The application modules are accessible from the project directory.

---

## 💡 Example Use Cases

### 1. Student Group Meetings

Students can upload recordings of project discussions and review:

- Tasks assigned to each member.
- Project decisions.
- Deadlines.
- Next meeting details.

### 2. Project Team Meetings

Teams can use the application to organize meeting reports and retrieve previously discussed information.

### 3. Academic Discussions

Students and researchers can use meeting summaries to revisit important discussion points and conclusions.

### 4. Personal Meeting Records

Users can maintain a searchable collection of analyzed meeting reports.

---

## 📊 Advantages of the Project

- Combines Generative AI with a practical use case.
- Uses a modular Python architecture.
- Includes database integration.
- Demonstrates RAG-based retrieval.
- Provides an interactive user interface.
- Supports storing multiple meeting reports.
- Can be extended with additional AI and productivity features.

---

## ⚠️ Limitations

The current implementation may have the following limitations:

- Analysis quality depends on audio clarity and the AI model.
- Speaker identification may not be available.
- Incorrect or incomplete audio transcription can affect the report.
- Local SQLite storage is not intended for large-scale multi-user deployment.
- API usage may be subject to provider limits and costs.
- Generated summaries and extracted information should be reviewed for accuracy.

---

## 🔮 Future Enhancements

The project can be improved with the following features:

### 🎤 1. Speaker Diarization

Identify different speakers and associate statements with individual participants.

### 📋 2. Automatic Action-Item Tracking

Extract assigned tasks and provide a dedicated action-item dashboard.

### 📅 3. Calendar Integration

Integrate with calendar services to track deadlines and schedule follow-up meetings.

### 📤 4. Report Export

Allow users to export meeting reports in formats such as:

- PDF
- DOCX
- TXT
- Markdown

### 🔐 5. User Authentication

Add user accounts and access control to protect private meeting information.

### ☁️ 6. Cloud Deployment

Deploy the application using cloud infrastructure and a production-ready database.

### 🌍 7. Multilingual Support

Support meetings conducted in multiple languages.

### 📈 8. Analytics Dashboard

Add analytics for:

- Number of meetings analyzed.
- Frequently discussed topics.
- Pending action items.
- Meeting trends.

### 🔎 9. Improved Retrieval

Improve document chunking, metadata filtering, and retrieval quality for large collections of meeting reports.

---

## 📚 Learning Outcomes

This project provides practical experience in:

- Python application development.
- Streamlit-based interface development.
- Generative AI API integration.
- Prompt-based AI workflows.
- Retrieval-Augmented Generation.
- Vector database concepts.
- SQLite database management.
- Modular software design.
- Environment variable management.
- Basic software testing.
- Version control using Git and GitHub.

---

## 🚀 Future Project Scope

MeetMind AI can be developed into a complete meeting productivity platform.

Potential advanced capabilities include:

- Real-time meeting analysis.
- Automated meeting minutes.
- Speaker identification.
- Intelligent task reminders.
- Team collaboration.
- Enterprise authentication.
- Cloud-based report storage.
- Advanced semantic search.
- Integration with productivity tools.

---

## 👨‍💻 Author

**Samridh Sagar**

Electronics and Communication Engineering Student  
Jaypee Institute of Information Technology, Noida

GitHub: [Samridh24](https://github.com/Samridh24)

---

## 📄 License

This project is developed for educational, learning, and portfolio purposes.

---

## ⭐ Support

If you find this project useful, consider giving the repository a star on GitHub.

Thank you for checking out **MeetMind AI!** 🚀
