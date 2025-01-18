import google.generativeai as genai

def enhance_text():

    genai.configure(api_key="AIzaSyB6FivWEBcB2FF5N7JLWqrHDCGAUW4ZTsU")
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content("Explain how AI works")
    print(response.text)

# Example usage
detailed_text = enhance_text()
print(detailed_text)
