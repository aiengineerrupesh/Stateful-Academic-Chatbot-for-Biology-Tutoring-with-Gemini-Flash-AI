from google import genai
from dotenv import load_dotenv
from google.genai import types
import os


def get_gemini_ai():
    load_dotenv()
    
    # Ensure API key exists
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY not found in .env file")
    
    return genai.Client(api_key=api_key)


def chat_with_gemini_ai(client, content_list):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            config=types.GenerateContentConfig(
                system_instruction="You are a helpful biology tutor"
            ),
            contents=content_list
        )

        # Safe return
        return response.text if response.text else "No response from AI"

    except Exception as e:
        return f"API Error: {e}"


def main():
    try:
        client = get_gemini_ai()
        content_list = []

        print("🧬 Biology Tutor AI (type 'exit' to quit)\n")

        while True:
            user_input = input("You: ").strip()

            if user_input.lower() == "exit":
                print("Goodbye 👋")
                break

            if not user_input:
                print("Please enter a valid question.")
                continue

            # Add user message
            content_list.append(
                types.Content(
                    role="user",
                    parts=[types.Part(text=user_input)]
                )
            )

            # Get AI response
            ai_replied = chat_with_gemini_ai(client, content_list)
            print("AI:", ai_replied)

            # Add AI response to history
            content_list.append(
                types.Content(
                    role="model",
                    parts=[types.Part(text=ai_replied)]
                )
            )

    except Exception as ex:
        print("Fatal Error:", ex)


if __name__ == "__main__":
    main()
