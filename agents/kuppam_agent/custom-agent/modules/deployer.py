import subprocess

def deploy_code(filename: str):
    print("🚀 Running the generated code...")
    try:
        subprocess.run(["python", filename], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Error running code: {e}")
