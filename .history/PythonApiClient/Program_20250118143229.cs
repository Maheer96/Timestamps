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

      // prompt is what the user says like "
      var prompt = "Bring me to World War 2"

        using var client = new HttpClient();
        var content = new StringContent(JsonSerializer.Serialize(new { name = "IS IN C SHARP" }), Encoding.UTF8, "application/json");

        var response = await client.PostAsync("http://127.0.0.1:5000/greet", content);
        var responseString = await response.Content.ReadAsStringAsync();

        Console.WriteLine(responseString); // Expected output: {"message":"Hello, World!"}
    }
}
