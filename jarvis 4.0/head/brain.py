import openai

# Set up your API key
openai.api_key = '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'

# Function to get response from ChatGPT
def get_chatgpt_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

# Example usage
user_input = "What are the benefits of using AI in healthcare?"
response = get_chatgpt_response(user_input)
print(response)



# Note: Make sure to handle your API key securely and not expose it in public code repositories.