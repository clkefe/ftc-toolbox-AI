from ollama import generate

PROMPT = '''
Function:
def get_relevant_docs(user_query: str):
    """
    Returns the most relevant documents from the Vector Database to user's query by doing vector similarity search.

    Args:
    user_query (string): the user query.

    Returns:
    list: The most relevant documents regarding to the user's query
    """
    
Function:
def no_relevant_function(user_query : str):
  """
  Call this when no other provided function can be called to answer the user query.

  Args:
     user_query: The user_query that cannot be answered by any other function calls.
  """

User Query: How is the weather in Istanbul?<human_end>
'''

response = generate('TEST_FUNCTION_CALLING', PROMPT)
ai_output = response['response']
print(ai_output)
