from GeminiAPI import GeminiAPI

def main():
    gemini_api = GeminiAPI()
    input_string = "Imagine a futuristic city with floating cars and neon lights."
    result = gemini_api.expand_string(input_string)
    print("Expanded Description:", result)

if __name__ == "__main__":
    main()