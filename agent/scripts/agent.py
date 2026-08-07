from openai import OpenAI
import argparse
import os
import sys
from dotenv import load_dotenv




load_dotenv()
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")

def create_agent(prompt):
    
    

    

    instr=open("../prompts/system.yaml").read()


    


    client=OpenAI(api_key=OPENAI_API_KEY)

    response = client.responses.create(
        model="gpt-4o-mini",
        input=prompt,
        instructions=instr
    )
    return response
  