import sys
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

def main():
    if len(sys.argv) < 2:
        print("No prompt was supplied, please add a prompt and rerun the program")
        sys.exit(1)
    else:
        verbose_mode = "--verbose" in sys.argv
        raw_args = sys.argv[1:]
        if verbose_mode:
            raw_args.remove("--verbose")
        content = " ".join(raw_args) 
        messages = [types.Content(role="user", parts=[types.Part(text=content)]),]
        print_response(messages, verbose_mode, content)


def print_response(content, verbose, prompt):
    response = client.models.generate_content(model='gemini-2.0-flash-001', contents=content)
    print(response.text)
    if verbose:
        if response.usage_metadata:
            prompt_token_count = response.usage_metadata.prompt_token_count
            candidates_token_count = response.usage_metadata.candidates_token_count

            print(f"User prompt: {prompt}")
            print(f"Prompt tokens: {prompt_token_count}")
            print(f"Response tokens: {candidates_token_count}")

if __name__ == "__main__":
    main()
