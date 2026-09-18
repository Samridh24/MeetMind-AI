
import os
import chromadb

from google import genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env")

client = genai.Client(api_key=API_KEY)

# Persistent ChromaDB storage
chroma_client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = chroma_client.get_or_create_collection(
    name="meeting_knowledge"
)


def create_embedding(text):
    """
    Convert text into a vector using Gemini embeddings.
    """

    response = client.models.embed_content(
        model="gemini-embedding-001",
        contents=text
    )

    return response.embeddings[0].values


def split_text(text, chunk_size=1000):
    """
    Split meeting report into smaller chunks.
    """

    chunks = []

    for i in range(0, len(text), chunk_size):

        chunk = text[i:i + chunk_size].strip()

        if chunk:
            chunks.append(chunk)

    return chunks


def store_meeting_report(report):
    """
    Store meeting report chunks in ChromaDB.
    """

    chunks = split_text(report)

    if not chunks:
        return 0

    embeddings = [
        create_embedding(chunk)
        for chunk in chunks
    ]

    # Unique IDs for each chunk
    import uuid

    ids = [
        str(uuid.uuid4())
        for _ in chunks
    ]

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings
    )

    return len(chunks)


def retrieve_relevant_chunks(question, n_results=3):
    """
    Retrieve relevant meeting information
    based on the user's question.
    """

    question_embedding = create_embedding(question)

    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=n_results
    )

    documents = results.get("documents", [[]])[0]

    return documents


def ask_meeting(question):
    """
    Answer user questions using retrieved context.
    """

    relevant_chunks = retrieve_relevant_chunks(question)

    if not relevant_chunks:
        return "No relevant information found in the meeting."

    context = "\n\n".join(relevant_chunks)

    prompt = f"""
You are a Meeting RAG Assistant.

Answer the user's question using ONLY
the retrieved meeting context below.

MEETING CONTEXT:
{context}

USER QUESTION:
{question}

Rules:
- Do not invent information.
- If the answer is not available, say:
  "This information is not available in the meeting."
- Give a clear and concise answer.
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text
import os
import uuid
import chromadb

from google import genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env")

client = genai.Client(api_key=API_KEY)


# Persistent ChromaDB storage
chroma_client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = chroma_client.get_or_create_collection(
    name="meeting_knowledge"
)


def create_embedding(text):
    """
    Convert text into a vector using Gemini embeddings.
    """

    response = client.models.embed_content(
        model="gemini-embedding-001",
        contents=text
    )

    return response.embeddings[0].values


def split_text(text, chunk_size=1000):
    """
    Split meeting report into smaller chunks.
    """

    chunks = []

    for i in range(0, len(text), chunk_size):

        chunk = text[i:i + chunk_size].strip()

        if chunk:
            chunks.append(chunk)

    return chunks


def store_meeting_report(report, meeting_id):
    """
    Store meeting report chunks in ChromaDB.

    Each chunk is associated with a specific meeting ID.
    """

    chunks = split_text(report)

    if not chunks:
        return 0

    embeddings = [
        create_embedding(chunk)
        for chunk in chunks
    ]

    ids = [
        str(uuid.uuid4())
        for _ in chunks
    ]

    metadatas = [
        {
            "meeting_id": str(meeting_id)
        }
        for _ in chunks
    ]

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings,
        metadatas=metadatas
    )

    return len(chunks)


def retrieve_relevant_chunks(
    question,
    meeting_id,
    n_results=3
):
    """
    Retrieve relevant chunks only from
    the selected meeting.
    """

    question_embedding = create_embedding(question)

    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=n_results,
        where={
            "meeting_id": str(meeting_id)
        }
    )

    documents = results.get("documents", [[]])[0]

    return documents


def ask_meeting(question, meeting_id):
    """
    Answer questions using only the selected
    meeting's retrieved context.
    """

    relevant_chunks = retrieve_relevant_chunks(
        question=question,
        meeting_id=meeting_id
    )

    if not relevant_chunks:
        return "No relevant information found in this meeting."

    context = "\n\n".join(relevant_chunks)

    prompt = f"""
You are a Meeting RAG Assistant.

Answer the user's question using ONLY
the retrieved meeting context below.

MEETING CONTEXT:
{context}

USER QUESTION:
{question}

Rules:
- Do not invent information.
- Use only the provided meeting context.
- If the answer is not available, say:
  "This information is not available in the meeting."
- Give a clear and concise answer.
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text