import requests
import json

def connect_to_perplexity(api_key: str, model: str, user_message: str) -> dict:
    url = "https://api.perplexity.ai/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": user_message}],
        "temperature": 0.2,
        "max_tokens": 100
    }
    
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()  # Raise an error for bad responses
    return response.json()

# Example usage
api_key = ""  # Replace with your actual API key
model = "llama-3.1-sonar-small-128k-online"  # Specify the model you want to use
user_message = "What is the latest news on the Indiana Pacers?"

response = connect_to_perplexity(api_key, model, user_message)
print(response['choices'][0]['message']['content'])
