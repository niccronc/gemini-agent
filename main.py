import argparse
import os

from google import genai
from google.genai import types

from tools.file_system_management import file_system_management_tools

SYSTEM_PROMPT = """
You are a helpful assistant. You are skilled in many topics.
When asked questions, you answer to the best of your abilities.
Do not make up information that you do not have, instead state very clearly what information you are missing.
"""

exit_command = '\exit'

def loading_gemini_api_key():
    """
    :return: GEMINI_API_KEY environment variable, if present. Throws a KeyError otherwise
    """
    try:
        gemini_api_key = os.environ["GEMINI_API_KEY"]
        return gemini_api_key
    except KeyError as e:
        print(f"Encountered exception {e} when loading the GEMINI_API_KEY environment variable.")

def initialize_gemini_client():
    """

    :return: instantiated Gemini client
    """
    api_key = loading_gemini_api_key()
    client = genai.Client(api_key=api_key)
    return client


def main():
    client = initialize_gemini_client()

    parser = argparse.ArgumentParser(description="Start interactive chat")
    parser.add_argument('--name', type=str, default='User', help='Your name')
    parser.add_argument('--model', type=str, default="gemini-2.0-flash", help='Gemini model version to use')
    args = parser.parse_args()

    chat = client.chats.create(
        model='gemini-2.0-flash',
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
            tools=file_system_management_tools
        ),
    )

    print(f"Hello {args.name}! How can I help you?")
    print(f"Type {exit_command} to leave the chat.\n")

    while True:
        try:
            user_input = input("You: ")
            if user_input.strip().lower() == exit_command:
                print("Goodbye!")
                break

            response = process_input(user_input, chat)
            print(f"Gemini: {response}")

        except KeyboardInterrupt:
            print("\nSession interrupted. Exiting...")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

def process_input(user_input, chat):
    response = chat.send_message(user_input)
    return response.text

if __name__ == '__main__':
    main()