import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
api_key = os.getenv("GEMINI_KEY")

genai.configure(api_key=api_key)

class Agent:
    def __init__(self, name, instructions, model_name="gemini-1.5-flash"):
        self.name = name
        self.instructions = instructions
        self.model = genai.GenerativeModel(model_name)

    def run(self, prompt: str) -> str:
        final_prompt = f"{self.instructions}\n\nUser: {prompt}"
        response = self.model.generate_content(final_prompt)
        return response.text

def main():
    agent = Agent(
        name="First Agent",
        instructions="You are a helpful assistant. you have to answer in a very simple way and short in hinglish"
    )
    prompt = input('Enter your question : ')
    result = agent.run(prompt)
    print(result)

if __name__ == "__main__":
    main()

