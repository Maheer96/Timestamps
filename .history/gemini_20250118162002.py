import google.generativeai as genai

async def enhance_text(prompt):
    genai.configure(api_key="AIzaSyB6FivWEBcB2FF5N7JLWqrHDCGAUW4ZTsU")
    
    # model = genai.GenerativeModel("gemini-1.5-flash")

    try:
        model = genai.GenerativeModel('gemini-pro')
        prompt = f"Generate me a brief paragraph (strictly a paragraph, not jots or anything else) that is less than 500 characters that visually describes the following prompt to Skybox AI to generate an accurate Skybox for the user. ONLY give me the paragraph and do not give any after-thoughts: '{input_string}'"
        response = await model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"An error occurred while expanding the description: {e}")
        return None

    response = model.generate_content("Explain how AI works")
    print(response.text)
    enhanced_prompt = response.text
    return enhanced_prompt

# Example usage
detailed_text = enhance_text("world war 2")
print(detailed_text)
