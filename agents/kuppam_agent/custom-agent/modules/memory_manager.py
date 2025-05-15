import json
import os

MEMORY_FILE = "memory/logs.json"

def save_to_memory(prompt: str, code: str):
    if not os.path.exists("memory"):
        os.makedirs("memory")
        
    if not os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "w") as f:
            json.dump([], f)

    with open(MEMORY_FILE, "r") as f:
        data = json.load(f)

    data.append({"prompt": prompt, "code": code})

    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=4)
    
    print("🧠 Prompt and code saved to memory.")
