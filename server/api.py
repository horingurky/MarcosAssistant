from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from core.brain import process_query

app = FastAPI()

app.mount("/static", StaticFiles(directory="server/static"), name="static")

@app.get("/ask")
def ask(q: str):
    return {"response": process_query(q)}
