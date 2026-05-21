import os
import asyncio
from dotenv import load_dotenv
from google import genai

# 1. Load configuration from your .env file
load_dotenv()

async def main():
    # 2. Initialize the modern Gemini Client
    # It automatically reads GEMINI_API_KEY from your environment variables
    client = genai.Client()
    
    # 3. Create a stateful chat session
    # We will use 'gemini-2.5-flash' as it is highly optimized for fast, multi-turn dialogue
    print("Initializing stateful conversation session...")
    chat = client.chats.create(model="gemini-2.5-flash")
    
    print("\n====================================================")
    # Give your agent an initial prompt or instructions if you want to test memory
    print("Gemini Agent Live! Type 'exit' or 'quit' to end the chat.")
    print("====================================================\n")
    
    while True:
        # 4. Capture native terminal input from the user
        user_input = input("You: ")
        
        # Check for break conditions
        if user_input.strip().lower() in ['exit', 'quit']:
            print("Ending conversation session. Goodbye!")
            break
            
        if not user_input.strip():
            continue

        try:
            # 5. Send message through the stateful chat object asynchronously
            # This automatically packages your new message with previous turns
            response = await asyncio.to_thread(chat.send_message, user_input)
            
            # 6. Print the continuous response stream out to the console
            print(f"\nAgent: {response.text}\n")
            
        except Exception as e:
            print(f"\nAn error occurred: {e}\n")

if __name__ == "__main__":
    # Run the main asynchronous execution loop
    asyncio.run(main())