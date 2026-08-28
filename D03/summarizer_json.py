# Day 3 - Summarizer with JSON Output (Ollama)
# 100% offline - uses llama3:8b local
import ollama
import json

def summerize(text: str):
    prompt = f"""
    Summerize the following text.
    Return the summary in JSON ONLY format like the following example:
    {{ "summary": "1 sentence", "bullets": ["point1", "point2", "point3"] }}
    Text: {text}
    """
    response = ollama.chat(
        model='llama3:8b',
        messages=[
            {'role': 'system', 'content': 'You are a helpful assistant that summerize text into JSON format.'},
            {'role': 'user', 'content': prompt}
        ],
        format='json'
    )
    content = response['message']['content']
# Day 3 - Summarizer with JSON Output (Ollama)
# 100% offline - uses llama3:8b local

import ollama
import json

def summarize(text: str):
    prompt = f"""
    Summarize the following text.
    Return JSON ONLY in this exact format:
    {{"summary": "1 sentence", "bullets": ["point1", "point2", "point3"]}}

    Text: {text}
    """
    response = ollama.chat(
        model='llama3:8b',
        messages=[{'role': 'user', 'content': prompt}],
        format='json'  # Ollama native JSON mode
    )
    content = response['message']['content']
    try:
        data = json.loads(content)
        print(f"Summary: {data['summary']}")
        for b in data['bullets']:
            print(f" - {b}")
        return data
    except Exception as e:
        print("Raw output:", content)
        print("Parse error:", e)

# Test
summarize("Python is a high-level programming language created by Guido van Rossum in 1991. It emphasizes readability and has vast libraries for AI, web, and automation.")
