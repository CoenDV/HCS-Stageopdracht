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

assistant = HCSInsuranceAssistant("model/granite-7b-instruct-Q4_K_M.gguf") # https://huggingface.co/tensorblock/granite-7b-instruct-GGUF

class PromptRequest(BaseModel):
    prompt: str

@app.post("/generate-with-RAG/")
async def generate_text_with_RAG(request: PromptRequest):
    return StreamingResponse(assistant.generate_response_with_RAG(request.prompt), media_type="text/plain")

@app.post("/generate-without-RAG/")
async def generate_text_without_RAG(request: PromptRequest):
    return StreamingResponse(assistant.generate_response_without_RAG(request.prompt), media_type="text/plain")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8080)