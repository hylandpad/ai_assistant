import os
import sys
import config
import functions.schema as schema
from functions.call_function import call_function
from functions.get_files_info import get_files_info
from dotenv import load_dotenv
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

from google import genai

client = genai.Client(api_key=api_key)

def make_request(messages, verbose=False):

    max_iterations = 20
    try:
        for i in range(max_iterations):

            response = client.models.generate_content(
                model='gemini-2.0-flash-001',
                contents=messages,
                config=types.GenerateContentConfig(tools=[schema.available_functions],system_instruction=config.SYSTEM_PROMPT),
            )

            for candidate in response.candidates:
                #print(candidate.content)
                messages.append(candidate.content)
                if hasattr(candidate, "text") and candidate.text:
                    print(candidate.text)
                    return
        
            if response.function_calls:
                function_call_result = call_function(response.function_calls[0], verbose)
                if function_call_result.parts[0].function_response.response:
                    function_response_content = types.Content(
                        role="user",
                        parts=[
                            types.Part(
                                function_response=types.FunctionResponse(
                                    name=function_call_result.parts[0].function_response.name, 
                                    response={
                                        "content": function_call_result.parts[0].function_response.response,
                                    }
                                )
                            )
                        ]
                    )
                    messages.append(function_response_content)
                    if verbose:
                        print(f"-> {function_call_result.parts[0].function_response.response}")
                else:
                    raise Exception("Function call failed - no response")
            
        user_prompt = f"User prompt: {sys.argv[1]}\n"
        candidates_tokens = f"Response tokens: {response.usage_metadata.candidates_token_count}\n"
        prompt_tokens = f"Prompt tokens: {response.usage_metadata.prompt_token_count}\n"

        if verbose == True:
            print(user_prompt + prompt_tokens + candidates_tokens)

    except Exception as e:
        print(f"Error: {e}")

def main():
    print("Hello from ai-assistant!")
    if len(sys.argv) < 2:
        print("No query provided, exiting program")
        sys.exit(1)
    else:
        verbose = "--verbose" in sys.argv
        args = [arg for arg in sys.argv[1:] if not arg.startswith("--") ]
        user_prompt = " ".join(args)
        messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)])]

        make_request(messages, verbose)
        
if __name__ == "__main__":
    main()
