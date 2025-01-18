import os
from typing import Optional
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# config the gem api
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

async def expand_description(input_string: str) -> Optional[str]:
    """
    expand user prompt with gem ai
    
    Args:
    input_string (str): string to be expanded.
    
    Returns:
    Optional[str]:  expanded description or None if an error occurs :))))
    """
    try:
        model = genai.GenerativeModel('gemini-pro')
        prompt = f"Generate me a brief paragraph (strictly a paragraph, not jots or anything else) that is less than 500 characters that visually describes the following prompt to Skybox AI to generate an accurate Skybox for the user. ONLY give me the paragraph and do not give any after-thoughts: '{input_string}'"
        response = await model.generate_content_async(prompt)
        return response.text
    except Exception as e:
        print(f"An error occurred while expanding the description: {e}")
        return None