from openai import OpenAI
import argparse
import os
import sys
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")

parser=argparse.ArgumentParser()

parser.add_argument("prompt", type=str)
parser.add_argument("--verbose",action="store_true")
args=parser.parse_args()
prompt=sys.argv[1]

instr=open("../prompts/system.yaml").read()


print(f"> {prompt}")

if args.verbose:
    print("thinking...")


client=OpenAI(api_key=OPENAI_API_KEY)

response = client.responses.create(
    model="gpt-4o-mini",
    input=prompt,
    instructions=instr
)

print(f"Token Output : {response.usage.output_tokens}")
print(response.output_text)



