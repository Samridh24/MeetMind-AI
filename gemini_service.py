
import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env")

client = genai.Client(api_key=API_KEY)


def analyze_meeting_audio(audio_path):

    # Upload audio to Gemini
    uploaded_file = client.files.upload(
        file=audio_path
    )

    prompt = """
You are an expert AI Meeting Intelligence Assistant.

Analyze the uploaded meeting audio.

Provide a structured and professional report.

1. EXECUTIVE SUMMARY
Summarize the meeting in 4-6 important points.

2. IMPORTANT DISCUSSIONS
Explain the major topics discussed.

3. DECISIONS TAKEN
List only decisions explicitly made.

4. ACTION ITEMS
For each task, identify:
- Task
- Assigned To
- Deadline
- Notes

If the person or deadline is unknown,
write Not Specified.

5. KEY TAKEAWAYS
List the most important outcomes.

6. FOLLOW-UP
Mention future meetings, pending tasks,
and next steps if discussed.

IMPORTANT:
- Do not invent information.
- Only use facts supported by the audio.
- Clearly distinguish confirmed decisions
  from suggestions.
- Keep the report easy to understand.
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=[
            uploaded_file,
            prompt
        ]
    )

    return response.text