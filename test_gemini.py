
import os
from dotenv import load_dotenv
from google import genai

# Load API key from .env
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env")

# Initialize Gemini
client = genai.Client(api_key=api_key)

# Test API request
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Explain RAG in one simple sentence."
)

print("Gemini API connected successfully!")
print("Response:", response.text)