import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai

# 1. Target the .env file inside your Setup folder
# Target the .env file located one level up in the parent directory's Setup folder
current_dir = Path(__file__).resolve().parent
env_path = current_dir.parent / "Setup" / ".env"
load_dotenv(dotenv_path=env_path)

# 2. Check that the Gemini key loaded successfully
if not os.getenv("GEMINI_API_KEY"):
    print("❌ Error: Could not find GEMINI_API_KEY. Check your Setup/.env file.")
else:
    print("✅ Gemini API Key loaded successfully.")
    
    # 3. Initialize the modern Google GenAI client
    # It automatically detects the GEMINI_API_KEY environment variable
    client = genai.Client()

    # 4. Request content from the model
    print("Sending test query to Gemini...")
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="How big is our solar system?"
    )

    print("\nGemini Response:")
    print(response.text)