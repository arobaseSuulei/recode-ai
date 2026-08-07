from agent import create_agent
from openai import OpenAI
import argparse
import os
import sys
from dotenv import load_dotenv







def main():

    load_dotenv()
    OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
    prompt,response = create_agent()

    

    while True:
        
        
        
        print(f"> {prompt}")
        if prompt in ("exit","q"):
            break

        
        
        print(f"Token Output : {response.usage.output_tokens}")
        print(response.output_text)

        user_input= input(">")

        if user_input in ("exit","q"):
            break

        client=OpenAI(api_key=OPENAI_API_KEY)
        instr=open("../prompts/system.yaml").read()

        response = client.responses.create(
            model="gpt-4o-mini",
            input=user_input,
            instructions=instr
        )

    
if __name__=="__main__":
    main()






