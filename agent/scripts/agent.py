from openai import OpenAI
import argparse
import os
import sys
from dotenv import load_dotenv
from pathlib import Path
import json
#from agent.tools.calcul import somme




load_dotenv()
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
PROMPT_PATH=Path(__file__).parent.parent /"prompts"/"system.yaml"
MEMORY_PATH=Path(__file__).parent.parent /"memory"/"memory.json"





def load_memory():
    with MEMORY_PATH.open("r", encoding="utf-8") as file:
        return json.load(file)


def add_memory(prompt,result):
    memory=load_memory()

    memory.extend(
    [{
        "role": "user",
        "content": prompt
    },
    {
        "role": "assistant",
        "content": result
    }
    ])

    with MEMORY_PATH.open("w",encoding="utf-8") as f:
        json.dump(memory, f, indent=4, ensure_ascii=True)


def create_agent(prompt):

    yield{
        "type":"start"
    }

    yield{
        "type":"loading_memory",
        "text":"reading memory..."
    }
    
    history=load_memory()
    
    instr=open(PROMPT_PATH).read()
    
    messages=history+[{"role":"user","content":prompt}]


    client=OpenAI(api_key=OPENAI_API_KEY)

    stream = client.responses.create(
        model="gpt-4o-mini",
        input=messages,
        instructions=instr,
        stream=True
        
    )
    full_response=""

    for event in stream:
        if event.type=="response.output_text.delta":
            yield{
                "type":"text_delta",
                "text":event.delta
            }
            
            full_response+=event.delta
    print()

    add_memory(prompt,full_response)

    yield{
        "type":"completed",
        "text":full_response
    }

  