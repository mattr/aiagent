import argparse
import os

from dotenv import load_dotenv
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

from google import genai

parser = argparse.ArgumentParser()
parser.add_argument("user_prompt")
parser.add_argument("-v", "--verbose",
                    help="Verbose: display information about the prompt and tokens",
                    action="store_true")

args = parser.parse_args()

system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories

All paths you provide should be relative to teh working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        }
    )
)

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
    ]
)

client = genai.Client(api_key=api_key)
response = client.models.generate_content(
    model='gemini-2.0-flash-001',
    contents=messages,
    config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt)
)

if len(response.function_calls) > 0:
    for function_call_part in response.function_calls:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
else:
    print(response.text)
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
