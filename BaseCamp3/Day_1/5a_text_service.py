from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware


# Create FastAPI instance with metadata for documentation
app = FastAPI(
    title="text API",
    description="A simple text API with processing",
    version="0.2.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development - restrict this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define Pydantic models for request validation
class TextInput(BaseModel):
    a: str = Field(..., description="Lengthy String")


    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "a": "Any lenghy string that spans more number of words",
                }
            ]
        }
    }



@app.post("/count")
def add(text: TextInput):
    """counts the number of words in the input text and returns the count."""
    result = len(text.a.split())
    return {f"length of string: {result} words"}


@app.post("/split")
def subtract(text: TextInput):
    """splits text into words and returns the list of words."""
    result = text.a.split()
    return result


@app.get("/")
def read_root():
    """Root endpoint that returns a welcome message."""
    return {"message": "text service API is running. Use /count or /split endpoints."}


# Main program
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9321)