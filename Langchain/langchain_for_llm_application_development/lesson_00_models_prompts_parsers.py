from utils import get_completion, get_completion_from_messages

def main():
    """
    Testing working of get_completion function.
    """
    response = get_completion("What is the capital of Srilanka?")
    if response:
        print(response)

if __name__ == "__main__":
    main()
    
