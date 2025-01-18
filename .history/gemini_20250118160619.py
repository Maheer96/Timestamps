import requests

def make_string_detailed(input_string):
    # Replace with the actual API endpoint and key
    API_ENDPOINT = "https://api.google.com/gemini"  # Replace with the real endpoint
    API_KEY = "your_api_key_here"  # Replace with your actual API key

    # Headers for the request
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    # Payload with the prompt
    prompt = f"Make the following text more detailed: {input_string}"
    payload = {
        "prompt": prompt,
        "max_tokens": 200,  # Adjust based on the desired length of the output
        "temperature": 0.7  # Adjust based on how creative the response should be
    }

    try:
        # Make the POST request
        response = requests.post(API_ENDPOINT, json=payload, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Parse the response
        data = response.json()
        return data.get("text", "No response text found")
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

# Example usage
input_text = "Rockets use thrust to overcome gravity."
detailed_text = make_string_detailed(input_text)
print(detailed_text)