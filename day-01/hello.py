import ollama

response = ollama.chat(
    model='llama3:8b',
    messages=[
        {'role': 'user', 'content': 'Explain Python functions like I am 5 years old'}
    ]
)

print(response['message']['content'])