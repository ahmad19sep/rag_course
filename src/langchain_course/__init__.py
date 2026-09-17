import os

from dotenv import load_dotenv

load_dotenv()



openai_api_key = os.environ.get("OPENAI_API_KEY")
anthropic_api_key = os.environ.get("ANTHROPIC_API_KEY")

def main() -> None:
    print(os.getcwd())
    print("Hello from langchain-course!")
    print(bool(openai_api_key))
    print(bool(anthropic_api_key))



if __name__ == "__main__":
    main()    