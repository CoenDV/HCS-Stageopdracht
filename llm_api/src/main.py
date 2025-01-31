from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from llm_utils import HCSInsuranceAssistant

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

assistant = HCSInsuranceAssistant("./../model/granite-3.0-8b-lab-community-Q4_K_M.gguf") # https://huggingface.co/bartowski/granite-3.0-8b-lab-community-GGUF

class PromptRequest(BaseModel):
    prompt: str
    correlation_id: str

@app.post("/generate-with-RAG/")
async def generate_text_with_RAG(request: PromptRequest):
    return StreamingResponse(assistant.generate_response_with_RAG(request), media_type="text/plain")

@app.post("/generate-without-RAG/")
async def generate_text_without_RAG(request: PromptRequest):
    return StreamingResponse(assistant.generate_response_without_RAG(request), media_type="text/plain")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8080)