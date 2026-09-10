import os
from dotenv import load_dotenv
from openai import OpenAI

# Load the API key from the .env file
load_dotenv()
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])


def get_embedding(text):
    """Convert a piece of text into an embedding (a list of numbers)."""
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding


def similarity(a, b):
    """Measure how similar two embeddings are (higher = more similar)."""
    return sum(x * y for x, y in zip(a, b))


# --- Our knowledge base (the "document" split into chunks) ---
chunks = [
    "Our office hours are Monday to Friday, 9 AM to 6 PM.",
    "Employees get 20 annual leave days per year.",
    "Parental leave is 12 weeks, fully paid.",
    "Remote work is allowed 2 days per week.",
    "The company provides health insurance for all full-time staff."
]

# === PHASE 1: Index the document (runs once) ===
# Convert every chunk into an embedding and store it in memory.
print("Preparing the knowledge base...")
chunk_embeddings = []
for chunk in chunks:
    chunk_embeddings.append(get_embedding(chunk))
print(f"Ready! Indexed {len(chunk_embeddings)} chunks.")

print("\nRAG assistant is ready. Type 'exit' to quit.")

# === PHASE 2: Answer questions (runs on every question) ===
while True:
    question = input("\nYour question: ")

    if question.lower() == "exit":
        print("Goodbye!")
        break

    # Step 1 - Retrieval: embed the question and find the most similar chunk
    question_embedding = get_embedding(question)

    scores = []
    for i in range(len(chunks)):
        score = similarity(question_embedding, chunk_embeddings[i])
        scores.append((score, chunks[i]))
    scores.sort(reverse=True)

    best_chunk = scores[0][1]

    # Step 2 - Augment + Generate: give the chunk to the AI and get an answer
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant. Answer ONLY using the context provided. If the answer is not in the context, say you don't know."},
            {"role": "user", "content": f"Context:\n{best_chunk}\n\nQuestion: {question}"}
        ]
    )

    print("\n=== Answer ===")
    print(response.choices[0].message.content)