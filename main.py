import os

import ollama
from dotenv import load_dotenv
load_dotenv()

MODEL_NAME = os.getenv("MODEL_NAME")

stream = ollama.chat(
    model=MODEL_NAME,
    messages=[{'role': 'user', 'content': 'Question: Why is the sky blue?'}],
    stream=True,
)

for chunk in stream:
  print(chunk['message']['content'], end='', flush=True)
