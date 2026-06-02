from fastapi import FastAPI
from fastapi.responses import FileResponse
from app.api.routes import router
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI(title="AI Career GPS Backend", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.get("/")
def root():
    # Serve index.html from app/static/index.html
    html_path = os.path.join(os.path.dirname(__file__), "static", "index.html")
    return FileResponse(html_path)
