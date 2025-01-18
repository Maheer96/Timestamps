using System.IO;
using Newtonsoft.Json.Linq;

namespace PromptEnhancer
{
    public class SecretsManager
    {
        public static string GetApiKey()
        {
            string filePath = "secrets.json";

            if (!File.Exists(filePath))
            {
                throw new FileNotFoundException("Secrets file not found.");
            }

            var jsonContent = File.ReadAllText(filePath);
            var jsonObject = JObject.Parse(jsonContent);
            return jsonObject["GeminiAPIKey"]?.ToString() 
                   ?? throw new Exception("API key not found in secrets.json.");
        }
    }
}

