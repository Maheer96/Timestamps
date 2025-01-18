from gemini_api import GeminiAPI

def main(
if __name__ == "__main__":
    API_URL = "https://api.gemini.com/v1/symbols/details" 
    API_KEY = "your_gemini_api_key_here"  

    # create instance of the api handler
    gemini = GeminiAPI(api_url=API_URL, api_key=API_KEY)

    # input string for expansion
    input_string = "A serene mountain landscape with a clear blue sky."

    # get expanded description
    expanded_description = gemini.expand_string(input_string)
    print("Expanded Description:", expanded_description)
