using System;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

namespace PromptEnhancer
{
    public class GeminiAPIHandler
    {
        // use a single shared instance of HttpClient to avoid exhausting system resources
        private static readonly HttpClient client = new HttpClient();

        // main function to interact with the Gemini API
        public async Task<string> GetGeminiResponseAsync(string input)
        {
            string apiUrl = "https://api.gemini.com/v1/symbols/details"; // Replace

            var payload = new
            {
                query = $"Generate me a brief paragraph (strictly a paragraph, not jots or anything else) that is less than 500 characters that visually describes the following prompt to Skybox AI to generate an accurate Skybox for the user. ONLY give me the paragraph and do not give any after-thoughts: {input}"
            };

            // serialize payload to JSON
            string jsonPayload = JsonConvert.SerializeObject(payload);

            try 
            {
                // create HTTP content for POST request
                var content = new StringContent(jsonPayload, Encoding.UTF8, "application/json");        
            
                // send POST request to Gemini API
                HttpResponseMessage response = await client.PostAsync(apiUrl, content);

                // make sure the response was successful
                response.EnsureSuccessStatusCode();

                // read response content as string
                string responseBody = await response.Content.ReadAsStringAsync();

                // deserialize the response into the GeminiResponse object
                var responseObject = JsonConvert.DeserializeObject<GeminiResponse>(responseBody);

                // return the description from the API response
                return responseObject.Description ?? "No description received.";
            }

            catch(Exception ex)
            {
                // handle any errors
                Console.WriteLine($"Error: {ex.Message}");
                return "An error occurred while fetching the Gemini response.";
            }
        }
    }

    public class GeminiResponse
    {
        [JsonProperty("description")]
        public string Description { get; set; }
    }
}