# Day 2 - Prompt Tester with Ollama
# pip install ollama
# Uses same model llama3:8b with 3 different system prompts

import ollama

SYSTEM_PROMPTS = {
    "coder": "You are a senior Python engineer. Answer with clean code only.",
    "analyst": "You are a data analyst. Explain insights clearly with examples.",
    "tutor": "You are a patient tutor. Explain like I'm 5 with analogies."
}

user_prompt = "What is a Python dictionary?"

for role, system in SYSTEM_PROMPTS.items():
    print(f"\n=== {role.upper()} ===")
    res = ollama.chat(
        model='llama3:8b',
        messages=[
            {'role': 'system', 'content': system},
            {'role': 'user', 'content': user_prompt}
        ]
    )
    print(res['message']['content'][:400])

# Save best prompts to /prompts/ for reuse
