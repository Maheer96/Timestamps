import google.generativeai as genai

def enhance_text(prompt):
    genai.configure(api_key="AIzaSyB6FivWEBcB2FF5N7JLWqrHDCGAUW4ZTsU")
    model = genai.GenerativeModel("gemini-1.5-flash")

    
    response = model.generate_content("Explain how AI works")
    print(response.text)
    enhanced_prompt = response.text
    return enhanced_prompt

# Example usage
detailed_text = enhance_text()
print(detailed_text)
