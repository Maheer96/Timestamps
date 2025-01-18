import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
secret_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=sec)


def enhance_text(input_string):
    model = genai.GenerativeModel("gemini-pro")

    try:
      prompt = f"Generate me a brief paragraph (strictly a paragraph, not jots or anything else) that is less than 500 characters that visually describes the following prompt to Skybox AI to generate an accurate Skybox for the user. ONLY give me the paragraph and do not give any after-thoughts: '{input_string}'"
      enhanced_prompt = model.generate_content(prompt).text
      
      return enhanced_prompt
    
    except Exception as e:
        print(f"An error occurred with getting the gemini response")
        return "World War 2 in battlefield when at night and in a rainy storm"


detailed_text = enhance_text("world war 2")
print(detailed_text)