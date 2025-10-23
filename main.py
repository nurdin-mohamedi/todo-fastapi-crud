from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def get_home() -> dict:
    return {"message": "Hello, World!"}
