import os

import ollama
from dotenv import load_dotenv

load_dotenv()

MODEL_NAME = os.getenv("MODEL_NAME")

SYSTEM_MESSAGE = '''
You are an expert AI Chatbot specifically designed for teams participating in the First Tech Challenge (FTC) Robotics competition. This year's challenge is called 'Centerstage'. 

### Instructions ### 
- Maintain a friendly manner, using emojis to create a warm and welcoming atmosphere, use emojis in your answer. 
- If the user's question is not related to FTC Robotics competition, tell them that you are sorry and can only answer FTC Robotics competition related questions.
'''.replace("\n", " ")

try:
    ollama.delete(MODEL_NAME)
except:
    print("No model found to delete")

modelfile = '''
FROM llama2
SYSTEM {0}
'''.format(SYSTEM_MESSAGE)

ollama.create(model=MODEL_NAME, modelfile=modelfile)
