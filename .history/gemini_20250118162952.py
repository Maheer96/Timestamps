import google.generativeai as genai
import os

# Suppress logging warnings
os.environ["GRPC_VERBOSITY"] = "ERROR"
os.environ["GLOG_minloglevel"] = "2"

genai.configure(api_key="AIzaSyB6FivWEBcB2FF5N7JLWqrHDCGAUW4ZTsU")

def enhance_text(input_string):
    model = genai.GenerativeModel("gemini-pro")

    try:
      prompt = f"Generate me a brief paragraph (strictly a paragraph, not jots or anything else) that is less than 500 characters that visually describes the following prompt to Skybox AI to generate an accurate Skybox for the user. ONLY give me the paragraph and do not give any after-thoughts: '{input_string}'"
      enhanced_prompt = model.generate_content(prompt).text
      #print(enhanced_prompt)
      
      return enhanced_prompt
    
    except Exception as e:
        print(f"An error occurred with getting the gemini response")
        return "World War 2 in battlefield when at night and in a rainy storm"


detailed_text = enhance_text("world war 2")
print(detailed_text)

print("\n\n\n\n")
