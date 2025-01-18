import requests
import json
from dotenv import load_dotenv
import os

class GeminiAPI:
    def __init__(self, api_url, api_key):
        """
        init. the gemini api with base url and api key

        api_url: endpoint of gemini api
        api_key: gemini key
        """

        self.api_url = api_url
        self.api_key = api_key

    def expand_string(self, input_string):
        """
        send a string to gemini ai for it to expand on

        input_string: the incoming string speech-to-text string
        """
        payload = {
            "query":f"Generate me a brief paragraph (strictly a paragraph, not jots or anything else) that is less than 500 characters that visually describes the following prompt to Skybox AI to generate an accurate Skybox for the user. ONLY give me the paragraph and do not give any after-thoughts: {input_string}"
        }

        headers = {
            "Content-Type" : "application/json",
            "Authorization" : f"Bearer {self.api_key}" # auth if needed
        }

        try:
            # Send the POST request
            response = requests.post(self.api_url, headers=headers, data=json.dumps(payload))
            response.raise_for_status()  # raise an error for HTTP errors

            # Parse and return the response
            response_data = response.json()
            expanded_string = response_data.get("description", "No description received.")
            return expanded_string

        except requests.exceptions.RequestException as e:
            return f"An error occurred while communicating with the Gemini API: {e}"
