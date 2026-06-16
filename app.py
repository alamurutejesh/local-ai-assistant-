from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import requests

app = FastAPI()

templates = Jinja2Templates(directory="templates")

# Chat memory
chat_history = []

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Home page
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )

# Ask AI
@app.get("/ask")
def ask(prompt: str, model: str = "mistral"):

    global chat_history

    chat_history.append(f"User: {prompt}")

    conversation = "\n".join(chat_history)

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": model,
            "prompt": conversation,
            "stream": False
        }
    )

    data = response.json()

    if "response" in data:

        answer = data["response"]

        chat_history.append(f"Assistant: {answer}")

        return {
            "response": answer,
            "history_length": len(chat_history)
        }

    return {
        "error": data
    }

# Clear memory
@app.get("/clear")
def clear_chat():

    global chat_history

    chat_history = []

    return {
        "message": "Chat history cleared"
    }