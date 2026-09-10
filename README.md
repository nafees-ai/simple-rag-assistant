# Simple RAG Assistant

A command-line Retrieval-Augmented Generation (RAG) assistant built with Python and the OpenAI API. It answers questions based only on a provided knowledge base, and clearly says "I don't know" when the answer is not found in the data.

## How It Works
1. **Indexing (once):** Each chunk of the knowledge base is converted into an embedding using OpenAI's `text-embedding-3-small` model and stored in memory.
2. **Retrieval:** When a question is asked, it is embedded and compared against all chunks using similarity scoring to find the most relevant one.
3. **Generation:** The most relevant chunk is passed to the language model as context, which generates an answer strictly based on that context.

## Features
- Semantic search (matches by meaning, not just keywords)
- Answers grounded strictly in the provided data (reduces hallucination)
- Interactive command-line loop until the user types `exit`
- Secure API key handling using a `.env` file

## Tech Stack
- Python
- OpenAI API (embeddings + chat completions)
- python-dotenv

## How to Run
1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `venv\Scripts\activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Create a `.env` file and add your key: `OPENAI_API_KEY=your_key_here`
6. Run: `python simple_rag.py`

## Author
Muhammad Nafees Khangit remote remove origin
