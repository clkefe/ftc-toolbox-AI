import os

import ollama
from dotenv import load_dotenv

load_dotenv()

MODEL_NAME = "TEST_FUNCTION_CALLING"

try:
    ollama.delete(MODEL_NAME)
except:
    print("No model found to delete")

modelfile = '''
FROM nexusraven
PARAMETER temperature 0.001
PARAMETER stop "Thought:"
'''

ollama.create(model=MODEL_NAME, modelfile=modelfile)
