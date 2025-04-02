from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv

load_dotenv()
hf_token = os.getenv("HUGGINGFACE_TOKEN")

client = InferenceClient(token=hf_token)

result = client.text_generation(
    "Привет, как твои дела?",
    model="mistralai/Mistral-7B-Instruct-v0.2"
)

print(result)