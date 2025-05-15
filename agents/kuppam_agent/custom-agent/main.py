from modules.prompt_handler import handle_prompt
from modules.code_writer import generate_code
from modules.deployer import deploy_code
from modules.memory_manager import save_to_memory

def main():
    prompt = input("💡 What do you want to build today?\n> ")
    task = handle_prompt(prompt)
    code = generate_code(task)
    filename = "generated_code.py"

    with open(filename, "w") as f:
        f.write(code)

    print(f"\n✅ Code saved to {filename}")
    deploy_code(filename)
    save_to_memory(prompt, code)

if __name__ == "__main__":
    main()
