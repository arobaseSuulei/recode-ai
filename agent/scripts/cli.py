from agent import create_agent
from openai import OpenAI
import argparse
import os
import sys
from dotenv import load_dotenv
from pathlib import Path
import json



def add_memory(prompt,result):
    
    file_path=Path(__file__).parent.parent /"memory"/"memory.json"
    with open(file_path, "r") as f:
        data = json.load(f)

    data.extend(
    [{
        "role": "user",
        "content": prompt
    },
    {
        "role": "assistant",
        "content": result
    }
    ])

    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

    return



def main():

    load_dotenv()
    OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")

    

    while True:

        prompt=input("> ")
        
        response=create_agent(prompt)

        if prompt in ("exit","q"):
            break

        result=response.output_text
        print(response.output_text)
        print(f"Token Output : {response.usage.output_tokens}")

        add_memory(prompt,result)
        





        

    
if __name__=="__main__":
    main()






