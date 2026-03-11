# Evaluating Chatbots
- In this exercise we are going to test the correctness of the chatbot responses.

# topics
    - Introduction
    - Installation and setup
    - Code workthrough
    - Observations

## Introduction
- When we talk about production grade application, we have to make sure that its reliable, and inorder to ensure its reliability, we have to perform observation on the application about how its performing. Doing so ensures the smooth functionin of the application and taking swift action in case of production issues, as monitoring and evaluation helps in pin-pointin the problem. 

## Installation and setup
- install `openai` and `langsmith` via pip or any other package manager tool(i.e uv)  
- Make sure that you have both langsmith and openai keys  
- Set up the environment variables
    - LANGSMITH_API_KEY
    - OPENAI_API_KEY"
    - LANGSMITH_TRACING

## Code walkthrough
- We start with setting up the environmental variables, followed by creating our test cases of inputs, outputs pair for evaluating the chatbot
- We define two test-parameters (correctness,conciseness) to test the chatbot correctness.
- We are oin to use LLM as judge evaluation technique.
- Finally we use different models to check the chatbot correctness by passing the test question, fetching the response from the chatbot and comparing it to the expected output results.

## Observations:
- The moment we want to create a chatbot, having evaluation setup done before production becomes crucial to ensure the chatbots correctness. Evaluation metrics helps us in understanding the weak-point of the chatbot and take corrective measures.
- Eventhough, in this example we have taken only two test-cases, it clearly showed its affectiveness, based on requirements we can have multiple test-scenarios.
- We also show the effectiveness in selecting the most appropriate model by model comparision against test outputs.
- In production environment, its very crucial to come up with most suitable LLM for your use-cases.4

