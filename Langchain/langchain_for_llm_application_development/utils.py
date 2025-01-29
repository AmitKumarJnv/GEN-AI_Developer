import os 
import openai
from typing import List, Dict
import logging
logging.basicConfig(level = logging.ERROR)

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())  # Read local environment files

# Creating variables 
openai.api_key = os.environ["OPENAI_API_KEY"]
llm_model = os.environ["OPENAI_MODEL"]

# for openai version > 1
client = openai.OpenAI()

def get_completion(prompt:str, model:str = llm_model) -> str:
    """
    Generates a response from the LLM for the given prompt.
    
    Args:
        prompt(str): The input prompt for LLM.
        model(str): The selected model

    Returns:
        str: The response generated from the LLM.
    """
    try:
        messages = [{"role": "user", "content": prompt}]
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0
        )
        return response.choices[0].message.content
    except Exception as e:
        logging.error(f"Error in get_completion(): {e}")
        return None

def get_completion_from_messages(messages: List[Dict[str,str]], model:str = llm_model, temperature:float = 0) -> str:
    """
    This fuction will take set of messages and seek llm response for it.

    Args:
        messages(List[Dict[str,str]]): List of messages for which we seek the LLM response.
        model(str): The selected model.
        temperature(float): Setting up the creativity value in LLM response.

    Returns:
        str: It returns LLM response.    
    """

    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature
        )
        return response.choices[0].message.content
    except Exception as e:
        logging.error(f"Error in get_completion_from_messages(): {e}")
        return None

if __name__ == "__main__":

    response = get_completion("What is the capital of India?")
    print(response)

