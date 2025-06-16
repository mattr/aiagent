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

messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

client = genai.Client(api_key=api_key)
response = client.models.generate_content(
    model='gemini-2.0-flash-001',
    contents=messages
)

print(response.text)
if args.verbose:
    print(f"User prompt: {args.user_prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
