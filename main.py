import sys
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import config
from functions.call_function import call_function
from functions.get_files_info import schema_get_files_info
from functions.write_file import schema_write_file
from functions.get_file_content import schema_get_file_content
from functions.run_python_file import schema_run_python_file

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


available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file,
    ]
)

def print_response(content, verbose, prompt):
    gen_config = types.GenerateContentConfig(tools=[available_functions], system_instruction=config.SYSTEM_PROMPT)
    response = client.models.generate_content(model='gemini-2.0-flash-001', contents=content, config=gen_config)
    if response.function_calls != None:
        function_call_responses = []
        for function in response.function_calls:
            function_call_results = call_function(function, verbose)
            if ( not function_call_results.parts
                or not function_call_results.parts[0].function_response
                or not function_call_results.parts[0].function_response.response
                ):
                raise Exception("fatal error")
            function_call_responses.append(function_call_results.parts[0])
            if verbose:
                print(f"-> {function_call_results.parts[0].function_response.response}")
        # print(function_call_responses)  

    else:
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
