from google import genai

def enhance_text(input_text):
    # Replace with your actual API key
    api_key = "AIzaSyB6FivWEBcB2FF5N7JLWqrHDCGAUW4ZTsU"

    # Initialize the Gemini client
    client = genai.Client(api_key=api_key)

    # Send the input text to the Gemini model
    response = client.models.generate_content(
        model="gemini-2.0-flash-exp",  # Specify the model to use
        contents=input_text
    )

    # Extract and return the generated detailed text
    return response.candidates[0].text

# Example usage
detailed_text = enhance_text("Describe the Eiffel Tower")
print(detailed_text)
