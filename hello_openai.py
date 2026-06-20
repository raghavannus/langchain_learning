import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

# 1. Point explicitly to the .env file inside your Setup folder
# Target the .env file located one level up in the parent directory's Setup folder
current_dir = Path(__file__).resolve().parent
env_path = current_dir.parent / "Setup" / ".env"
load_dotenv(dotenv_path=env_path)

# 2. Verify the key was read correctly before calling the API
if not os.getenv("OPENAI_API_KEY"):
    print("❌ Error: Could not find OPENAI_API_KEY. Check your Setup/.env file.")
else:
    print("✅ API Key loaded successfully.")
    
    # 3. Initialize the OpenAI client
    client = OpenAI()

    # 4. Make the call using a modern, fast reasoning model
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # Upgraded from 3.5-turbo for better performance
        messages=[
            {"role": "user", "content": "What is the capital of France?"}
        ]
    )

    print("\nLLM Response:")
    print(response.choices[0].message.content)