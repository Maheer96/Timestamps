import google.generativeai as genai

async def enhance_text(prompt):
    genai.configure(api_key="AIzaSyB6FivWEBcB2FF5N7JLWqrHDCGAUW4ZTsU")
    model = genai.GenerativeModel("gemini-pro")

    try:
      response = model.generate_content("Explain how AI works")
      print(response.text)
      enhanced_prompt = response.text
      return enhanced_prompt
    except Exception as e:
        print(f"An error occurred while expanding the description: {e}")
        return "World War 2 in battlefield"

# Example usage
detailed_text = enhance_text("world war 2")
print(detailed_text)
