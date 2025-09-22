from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/add")
def add(a: int, b: int):
    return {"result": a + b}

@app.get("/subtract")
def subtract(a: int, b: int):
    return {"result": a - b}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9321)
    print("Server started at {http://localhost:9321/docs} ")