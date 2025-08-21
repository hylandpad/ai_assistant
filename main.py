import os
import sys
import argparse
from dotenv import load_dotenv
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

from google import genai

client = genai.Client(api_key=api_key)

def test_call(messages, verbose=False):

    response = client.models.generate_content(model='gemini-2.0-flash-001',contents=messages)
    
    response_text = f"{response.text}\n"
    user_prompt = f"User prompt: {sys.argv[1]}\n"
    candidates_tokens = f"Response tokens: {response.usage_metadata.candidates_token_count}\n"
    prompt_tokens = f"Prompt tokens: {response.usage_metadata.prompt_token_count}\n"
    
    print(response_text)

    if verbose == True:
        print(user_prompt + prompt_tokens + candidates_tokens)

def main():
    print("Hello from ai-assistant!")
    if len(sys.argv) < 2:
        print("No query provided, exiting program")
        sys.exit(1)
    else:
        user_prompt = " ".join(sys.argv[1])

        messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)])]
        verbose = "--verbose" in sys.argv
        
        test_call(messages, verbose)
        
if __name__ == "__main__":
    main()
