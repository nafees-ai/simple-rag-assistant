import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

print("=== Smart Reply Generator ===")
print("(Kabhi bhi 'exit' likh kar band kar sakte hain)\n")

while True:
    # 1. User se woh message lo jiska reply chahiye

    message = input("Jis message ka reply chahiye woh paste karein:\n")

    if message.strip().lower() == "exit":
        print("\nAlvida! Program band ho raha hai.")
        break

    # 2. Tone choose karwao
    print("\nTone choose karein:")
    print("1 = Professional")
    print("2 = Friendly")
    print("3 = Short")
    choice = input("Number likhein (1/2/3): ")

    if choice.strip().lower() == "exit":
        print("\nAlvida! Program band ho raha hai.")
        break

    # 3. Choice ke hisaab se system prompt (routing!)
    if choice == "1":
        system_prompt = "You are a professional assistant. Write a polite, formal reply."
    elif choice == "2":
        system_prompt = "You are a friendly assistant. Write a warm, casual reply."
    elif choice == "3":
        system_prompt = "You are concise. Write a very short, direct reply (2-3 lines max)."
    else:
        system_prompt = "You are a helpful assistant. Write a clear reply."

    # 4. AI se reply generate karwao
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Write a reply to this message:\n{message}"}
        ]
    )

    # 5. Reply print karo
    print("\n--- Aap ka Reply ---")
    print(response.choices[0].message.content)
    print("\n" + "=" * 40 + "\n")
