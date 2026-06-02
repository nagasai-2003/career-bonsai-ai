from fastapi import FastAPI
from fastapi.responses import FileResponse
from app.api.routes import router
import os

app = FastAPI(title="AI Career GPS Backend", version="1.0")

app.include_router(router)

@app.get("/")
def root():
    # Serve index.html from app/static/index.html
    html_path = os.path.join(os.path.dirname(__file__), "static", "index.html")
    return FileResponse(html_path)
