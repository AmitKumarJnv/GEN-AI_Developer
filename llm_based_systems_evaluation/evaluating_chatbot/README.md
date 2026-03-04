# Evaluating Chatbots

# topics
## Introduction
## Installation and setup
## Code workthrough
## Observations

## Introduction
- When we talk about production grade application, we have to make sure that its reliable, and inorder to ensure its reliability, we have to perform observation on the application about how its performing. Doing so ensures the smooth functionin of the application and taking swift action in case of production issues, as monitoring and evaluation helps in pin-pointin the problem. 

## Installation and setup
- install `openai` and `langsmith` via pip or any other package manager tool(i.e uv)  
- Make sure that you have both langsmith and openai keys  
- Set up the environment variables
    - os.environ["LANGSMITH_API_KEY"]=os.getenv("LANGSMITH_API_KEY")
    - os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
    - os.environ["LANGSMITH_TRACING"]="true"

