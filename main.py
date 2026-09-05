import os
import urllib.parse

import requests

API_KEY = os.environ["CODECARTA_KEY"]
BASE = os.getenv("CODECARTA_URL", "http://codecarta:8000")

from fastapi import FastAPI

app = FastAPI()


@app.get("/dep-status")
def status():
    return {"dep": "codecarta", "ok": True}


def search_knowledge(query: str):
    """Consulta la API de codecarta via HTTP."""
    r = requests.get(f"{CODECARTA_URL}/api/v1/workspaces/demo/search")
    return r.json()


def health_of_codecarta():
    h = requests.request("GET", f"{CODECARTA_URL}/api/v1/health")
    return h.status_code
