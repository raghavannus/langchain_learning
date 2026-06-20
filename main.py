import os
from pathlib import Path

from dotenv import load_dotenv

# 1. Dynamically find the parent folder to reach Setup/
current_dir = Path(__file__).resolve().parent
env_path = current_dir.parent / "Setup" / ".env"
load_dotenv(dotenv_path=env_path)

def main():
    print("Hello from langchain-course!")


if __name__ == "__main__":
    main()