from pymilvus import MilvusClient
from sentence_transformers import SentenceTransformer
from glob import glob
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import milvus_utils
import minio_utils
from models import SearchRequest

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

milvus = milvus_utils.milvus_utils("http://milvus-standalone", "19530")
minio = minio_utils.minio_utils("milvus-minio:9000", "minioadmin", "minioadmin")

@app.post("/prepare/")
async def generate_text():
    return milvus.load_documents()

@app.post("/search/")
async def search_text(request: SearchRequest):
    return milvus.search(request)

@app.post("/load-minio/")
async def load_documents():
    return minio.load_documents()

@app.get("/documents/")
async def get_documents():
    return minio.get_documents()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8080)