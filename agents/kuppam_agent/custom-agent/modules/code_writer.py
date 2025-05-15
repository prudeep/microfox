from openai import OpenAI

client = OpenAI(
    base_url="http://127.0.0.1:1234",
    api_key="lm-studio"
)

def generate_code(task):
    try:
        response = client.completions.create(
            model="deepseek-r1-distill-qwen-7b",  # Ensure this matches exactly in LM Studio
            messages=[{"role": "user", "content": task}],
            temperature=0.7,
            max_tokens=500
        )

        print("\n🛠️ Full API Response:\n", response)

        if not response or not response.choices or not hasattr(response.choices[0], "message"):
            raise ValueError("Invalid or empty chat response structure.")

        code = response.choices[0].message.content.strip()
        print("\n✅ Generated Code:\n", code)
        return code

    except Exception as e:
        print(f"\n❌ Error generating code: {e}")
        return "# Error: Unable to generate code"
