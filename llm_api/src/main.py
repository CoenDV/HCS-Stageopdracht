from fastapi import FastAPI, HTTPException
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

assistant = HCSInsuranceAssistant("./../model/granite-7b-lab-Q4_K_M.gguf")

class PromptRequest(BaseModel):
    prompt: str

@app.post("/generate/")
async def generate_text(request: PromptRequest):
    return {"response": assistant.generate_response(request.prompt)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8080)