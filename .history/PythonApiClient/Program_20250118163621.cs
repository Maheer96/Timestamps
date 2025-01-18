using System;
using System.Net.Http;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;

// the c-sharp code in unity

class Program
{
    static async Task Main(string[] args)
    {

      // prompt is what the user says like "show me the stone age"
      var prompt = "Show me the stone age";

      // create request payload to send to python/flask endpoint
      using var client = new HttpClient();
      var content = new StringContent(JsonSerializer.Serialize(new { prompt = prompt }), Encoding.UTF8, "application/json");

      // send prompt to python function and store response (enhanced prompt)
      var response = await client.PostAsync("http://127.0.0.1:5000/greet", content);
      var responseString = await response.Content.ReadAsStringAsync();

      // handle and use the enhanced prompt
      Console.WriteLine(responseString); // Expected output: {"message":"Hello, World!"}
    }
}
