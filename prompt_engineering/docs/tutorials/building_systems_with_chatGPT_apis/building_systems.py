import openai 

# load the environment variable, create a .env file and store your OPENAI_API_KEY in that file
from dotenv import load_dotenv
load_dotenv()

# for openai version > 1
client = openai.OpenAI()

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0
    )
    return response.choices[0].message.content

def get_completion_from_messages(messages, model="gpt-3.5-turbo",temperature=0):
    messages = messages
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature
    )
    return response.choices[0].message.content

if __name__ == "__main__":

    # response = get_completion("What is the capital of France?")
    # print(response)

    response = get_completion("What is the capital of India?")
    print(response)