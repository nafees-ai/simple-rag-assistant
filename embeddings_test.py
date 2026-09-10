import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

# Ek chhota function jo kisi text ka embedding laa de
def get_embedding(text):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding

# Teen words ke embeddings banao
dog = get_embedding("king")
puppy = get_embedding("queen")
banana = get_embedding("banana")

# Do embeddings kitne "paas" hain, yeh naapने ka tareeqa (similarity)
def similarity(a, b):
    # dot product: dono lists ko multiply kar ke jodo
    return sum(x * y for x, y in zip(a, b))

# Compare karo
print("king vs queen:", similarity(dog, puppy))
print("king vs banana:", similarity(dog, banana))