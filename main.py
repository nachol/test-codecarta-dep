import os
API_KEY = os.environ["CODECARTA_KEY"]
BASE = os.getenv("CODECARTA_URL", "http://codecarta:8000")

from fastapi import FastAPI
app = FastAPI()

@app.get("/dep-status")
def status():
    return {"dep": "codecarta", "ok": True}
