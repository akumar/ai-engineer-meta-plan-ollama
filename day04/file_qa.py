import ollama

# 1. Read file
file_path = "day04/sample_notes.txt"
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 2. Token management - truncate if too long
if len(content) > 4000:
    content = content[:4000]
    print("(Note: File truncated to 4000 chars for token limit)")

# 3. Ask question
question = input("Ask a question about the file: ")

# 4. Send to Ollama with strict context prompt
response = ollama.chat(
    model='llama3:8b',
    messages=[
        {
            'role': 'system', 
            'content': f'You are a file assistant. Answer ONLY from this file content. If answer not in file, say "Not found in file".\n\nFile Content:\n{content}'
        },
        {'role': 'user', 'content': question}
    ]
)

print("\n--- Answer ---")
print(response['message']['content'])