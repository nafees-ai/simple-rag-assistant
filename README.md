# Smart Reply Generator

A command-line AI tool that generates replies to any message in a chosen tone.
Paste a message, pick a tone (Professional, Friendly, or Short), and the
assistant writes a suitable reply using the OpenAI API.

## Features
- Interactive command-line interface
- Three reply tones with runtime prompt routing (Professional / Friendly / Short)
- Loops for continuous use until you type `exit`
- Secure API key handling using a `.env` file

## Tech Stack
- Python
- OpenAI API
- python-dotenv

## How to Run
1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `venv\Scripts\activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Create a `.env` file and add your key: `OPENAI_API_KEY=your_key_here`
6. Run: `python reply_generator.py`

## Author
Muhammad Nafees Khan