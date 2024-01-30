from ollama import generate

PROMPT = '''    
Function:
def get_team_id(team_name: str):
  """
  Returns the First Tech Challenge team's ID by searching in the vector database

  Args:
     team_name: The First Tech Challenge (FTC) team name that is provided in the user query.
     
  Returns:
    int: The FTC team's ID
  """
    
Function:
def get_team_stats(team_id: int):
  """
  Returns the stats for a First Tech Challenge team. Call this only when the user query specifically asks for a team's stats. 

  Args:
     team_id: The First Tech Challenge (FTC) team ID
     
  Returns:
    string: the stats of the FTC team
  """
  
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
def no_relevant_function(user_query: str):
  """
  Call this when no other provided function can be called to answer the user query.

  Args:
     user_query: The user_query that cannot be answered by any other function calls.
  """

User Query: How is the Huskyteers doing this season?<human_end>
'''

# Ex user query: What is considered as knocking down the pixels during the driver controlled period?

response = generate('TEST_FUNCTION_CALLING', PROMPT)
ai_output = response['response']
print(ai_output)
