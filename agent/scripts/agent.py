from openai import OpenAI
import argparse
import os
import sys
from dotenv import load_dotenv




load_dotenv()
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")

def create_agent():
    parser=argparse.ArgumentParser() #args for the input prompt user

    parser.add_argument("prompt", type=str)
    parser.add_argument("--verbose",action="store_true") #verbose for showing what the model is doing
    
    args=parser.parse_args()
    prompt=sys.argv[1]

    

    instr=open("../prompts/system.yaml").read()


    


    client=OpenAI(api_key=OPENAI_API_KEY)

    response = client.responses.create(
        model="gpt-4o-mini",
        input=prompt,
        instructions=instr
    )
    return prompt,response
  