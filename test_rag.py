
from rag_service import (
    create_embedding,
    store_meeting_report,
    retrieve_relevant_chunks
)

print("Testing Gemini Embeddings...")

text = "The marketing team will submit the project report by Friday."

embedding = create_embedding(text)

print("Embedding created successfully!")
print("Vector dimensions:", len(embedding))


print("\nTesting ChromaDB storage...")

chunks_stored = store_meeting_report(text)

print("Chunks stored:", chunks_stored)


print("\nTesting retrieval...")

results = retrieve_relevant_chunks(
    "When will the project report be submitted?"
)

print("Retrieved information:")
print(results)