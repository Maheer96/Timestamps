from google import genai

def enhance_text(input_text):
    import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Explain how AI works")
print(response.text)

# Example usage
detailed_text = enhance_text("Describe the Eiffel Tower")
print(detailed_text)
