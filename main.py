from fastapi import FastAPI
from dotenv import load_dotenv
import uvicorn
from app.api.chat_api import router

load_dotenv()

app = FastAPI()
app.include_router(router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)