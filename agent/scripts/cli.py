from agent import create_agent
from openai import OpenAI
import argparse
import os
import sys
from dotenv import load_dotenv







def main():

    load_dotenv()
    OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
    

    

    while True:

        prompt=input("> ")
        
        response=create_agent(prompt)

        if prompt in ("exit","q"):
            break

        
        print(response.output_text)
        print(f"Token Output : {response.usage.output_tokens}")

        

    
if __name__=="__main__":
    main()






