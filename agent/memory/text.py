from pathlib import Path
import json

file_path=Path(__file__).parent / "memory.json"

with open(file_path,"r") as f:
    data=json.load(f)
print(data[0]["content"])