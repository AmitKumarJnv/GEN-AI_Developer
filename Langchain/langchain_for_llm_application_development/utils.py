import os 
import openai

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())  # Read local environment files

# Creating variables 
openai.api_key = os.environ["OPENAI_API_KEY"]
llm_model = os.environ["OPENAI_MODEL"]

# for openai version > 1
client = openai.OpenAI()

def get_completion(prompt, model=llm_model):
    """This function will take a prompt and return chatgpt response"""
    try:
        messages = [{"role": "user", "content": prompt}]
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0
        )
        return response.choices[0].message.content
    except Exception as e:
        print(e)

def get_completion_from_messages(messages, model=llm_model,temperature=0):
    """This fuction will take set of messages and seek llm response for it"""

    try:
        messages = messages
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature
        )
        return response.choices[0].message.content
    except Exception as e:
        print(e)

if __name__ == "__main__":

    response = get_completion("What is the capital of India?")
    print(response)

