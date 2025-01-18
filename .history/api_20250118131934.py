from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from gemini_expander import expand_description

app = FastAPI()

class InputString(BaseModel):
    text: str

class ExpandedDescription(BaseModel):
    expanded_text: str

@app.post("/expand", response_model=ExpandedDescription)
async def expand_text(input_string: InputString):
    """
    endpt to expand a given input string using Gemini AI.
    """
    expanded = await expand_description(input_string.text)
    if expanded is None:
        raise HTTPException(status_code=500, detail="Failed to expand the description")
    return ExpandedDescription(expanded_text=expanded)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)