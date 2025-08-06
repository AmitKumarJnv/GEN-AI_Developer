from utils import get_completion, get_completion_from_messages
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
model = ChatOpenAI(model="gpt-4o-mini")

def main():
    """
    Testing working of get_completion function.
    """
    response = get_completion("What is the capital of Srilanka?")
    if response:
        return response

def without_prompt_template()->str:
    """
    Performing some task without any prompt template.
    """  
    customer_email = """
        Arrr, I be fuming that me blender lid \
        flew off and splattered me kitchen walls \
        with smoothie! And to make matters worse,\
        the warranty don't cover the cost of \
        cleaning up me kitchen. I need yer help \
        right now, matey!
        """      
    
    style = """American English \
        in a calm and respectful tone
        """
    
    prompt = f"""Translate the text \
        that is delimited by triple backticks 
        into a style that is {style}.
        text: ```{customer_email}```
        """
    
    response = get_completion(prompt)

    return response

def langchain_prompt_template()->str:
    """
    Creating Prompt Templates.
    """

    template_string = """Translate the text \
        that is delimited by triple backticks \
        into a style that is {style}. \
        text: ```{text}```
        """
    
    prompt_template = PromptTemplate.from_template(template_string)

    customer_email = """
        Arrr, I be fuming that me blender lid \
        flew off and splattered me kitchen walls \
        with smoothie! And to make matters worse,\
        the warranty don't cover the cost of \
        cleaning up me kitchen. I need yer help \
        right now, matey!
        """      
    
    style = """American English \
        in a calm and respectful tone
        """
    
    data = prompt_template.invoke({"style":style,"text":customer_email})

    return get_completion(data.text)

if __name__ == "__main__":
    print(main())
    
