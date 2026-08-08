from openai import OpenAI
import argparse
import os
import sys
from dotenv import load_dotenv
from pathlib import Path
import json




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
    history=load_memory()
    instr=open(PROMPT_PATH).read()
    
    messages=history+[{"role":"user","content":prompt}]


    client=OpenAI(api_key=OPENAI_API_KEY)

    response = client.responses.create(
        model="gpt-4o-mini",
        input=messages,
        instructions=instr
    )
    add_memory(prompt,response.output_text)
    return response
  