import os
from typing import Optional
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# confi the Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

async def expand_description(input_string: str) -> Optional[str]:
    """
    Expands the given input string using the Gemini AI API.
    
    Args:
    input_string (str): string to be expanded.
    
    Returns:
    Optional[str]:  expanded description or None if an error occurs :))))
    """
    try:
        model = genai.GenerativeModel('gemini-pro')
        prompt = f"Please expand on the following text and make it more descriptive: '{input_string}'"
        response = await model.generate_content_async(prompt)
        return response.text
    except Exception as e:
        print(f"An error occurred while expanding the description: {e}")
        return None