import os
import asyncio
from google import genai
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

async def run_chat_session():
    print("\n" + "="*50)
    print("      PLACEMENT COACH AGENT - DAY 1 ACTIVE      ")
    print("="*50)
    print("Type your message and press Enter. (Type 'exit' or 'quit' to stop)\n")

    # Fetch the API key safely from environment variables
    api_key = os.environ.get("GEMINI_API_KEY")

    try:
        # Standard initialization (No alpha version tags)
        client = genai.Client(api_key=api_key)
    except Exception as e:
        print(f"Initialization Error: {e}")
        return

    # Use the globally available flash model 
    model_id = 'gemini-2.5-flash'
    
    # Initialize a fresh chat session
    chat = client.chats.create(model=model_id)

    while True:
        try:
            user_input = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nSession ended cleanly.")
            break

        # Check for termination commands
        if user_input.lower() in ['exit', 'quit']:
            print("Goodbye! Best of luck with your placement prep!")
            break

        if not user_input:
            continue

        print("\nCoach is thinking...")
        
        try:
            # Send message to Google AI Studio backend
            response = chat.send_message(user_input)
            print(f"\nCoach: {response.text}\n")
            print("-" * 50)
        except Exception as e:
            print(f"\nAn error occurred while connecting to the server:")
            print(f"Details: {e}")
            print("-" * 50)

if __name__ == "__main__":
    asyncio.run(run_chat_session())