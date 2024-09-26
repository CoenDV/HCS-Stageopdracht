from pymilvus import MilvusClient, Collection, connections
from sentence_transformers import SentenceTransformer
from glob import glob
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/prepare/")
async def generate_text():
    
    milvus_client = MilvusClient(
        uri='http://172.30.24.69',
        port='19530',
    )

    # create collection
    if milvus_client.has_collection("demo_collection"):
        milvus_client.drop_collection("demo_collection")

    milvus_client.create_collection(
        collection_name="demo_collection", 
        dimension=384,
        metric_type="IP",
        index_type="IVF_FLAT",
    )

    # prepare documents
    print("Preparing documents...")
    model = SentenceTransformer('all-MiniLM-L6-v2')
    docs = []
    vectors = []

    for file_path in glob("./../vectordb/documents/*.txt", recursive=True):
        with open(file_path, "r") as file:
            file_text = file.read()
            docs.append(file_text)
            vectors.append(model.encode(file_text))

    data = [
        {"id": i, "vector": vectors[i], "text": docs[i], "subject": "insurance"}
        for i in range(len(vectors))
    ]

    # insert data
    print("Inserting data...")
    res = milvus_client.insert(collection_name="demo_collection", data=data)
    print(milvus_client.describe_collection("demo_collection"))
    print(res)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8080)