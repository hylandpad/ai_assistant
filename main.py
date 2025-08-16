import os
import sys
from dotenv import load_dotenv


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

from google import genai

client = genai.Client(api_key=api_key)

def test_call():

    response = client.models.generate_content(model='gemini-2.0-flash-001',contents=f"{sys.argv[1]}")
    
    response_text = f"{response.text}\n"
    candidates_tokens = f"Response tokens: {response.usage_metadata.candidates_token_count}\n"
    prompt_tokens = f"Prompt tokens: {response.usage_metadata.prompt_token_count}\n"
    print(response_text + "\n" + prompt_tokens + candidates_tokens)
    


def main():
    print("Hello from ai-assistant!")
    if len(sys.argv) < 2:
        print("No query provided, exiting program")
        sys.exit(1)
    else:
        test_call()


if __name__ == "__main__":
    main()
