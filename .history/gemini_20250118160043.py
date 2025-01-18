import os
from typing import Optional
import google.generativeai as genai

# config the gem api
genai.configure(api_key="AIzaSyB6FivWEBcB2FF5N7JLWqrHDCGAUW4ZTsU")

async def expand_description(input_string):

    # expand user prompt with gem ai
    
    try:
        model = genai.GenerativeModel('gemini-pro')
        prompt = f"Generate me a brief paragraph (strictly a paragraph, not jots or anything else) that is less than 500 characters that visually describes the following prompt to Skybox AI to generate an accurate Skybox for the user. ONLY give me the paragraph and do not give any after-thoughts: '{input_string}'"
        response = await model.generate_content_async(prompt)
        return response.text
    except Exception as e:
        print(f"An error occurred while expanding the description: {e}")
        return "Imagine you are on a world war 2 battlefiled and it is the night and it is raining"
    


expand_description("world war 2")