using System;
using System.Net.Http;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        using var client = new HttpClient();
        var content = new StringContent(JsonSerializer.Serialize(new { name = "World" }), Encoding.UTF8, "application/json");

        var response = await client.PostAsync("http://127.0.0.1:5000/greet", content);
        var responseString = await response.Content.ReadAsStringAsync();

        Console.WriteLine(responseString); // Expected output: {"message":"Hello, World!"}
    }
}
