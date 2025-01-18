import aiohttp
import asyncio

async def get_expanded_description(text: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.post("http://localhost:8000/expand", json={"text": text}) as response:
            if response.status == 200:
                data = await response.json()
                return data["expanded_text"]
            else:
                return f"Error: {response.status}"

async def main():
    input_text = "The cat sat on the mat."
    expanded = await get_expanded_description(input_text)
    print(f"Original: {input_text}")
    print(f"Expanded: {expanded}")

if __name__ == "__main__":
    asyncio.run(main())