from gemini_api import GeminiAPI

def main():
    gemini_api = GeminiAPI()
    input_string = ""
    result = gemini_api.expand_string(input_string)
    print("Expanded Description:", result)

if __name__ == "__main__":
    main()