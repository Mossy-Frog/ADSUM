from fastapi import FastAPI

app = FastAPI() #uvicorn main_fastapi:app --reload


@app.get("/")
async def root():
    return {"message": "Hello World"}