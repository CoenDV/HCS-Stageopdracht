from pymilvus import MilvusClient
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
from glob import glob
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

milvus_uri = "http://milvus-standalone" # Change this to the IP address of your Milvus server
model = SentenceTransformer('all-MiniLM-L6-v2', cache_folder='/app/.cache')

@app.post("/prepare/")
async def generate_text():
    milvus_client = MilvusClient(
        uri=milvus_uri,
        port="19530",
    )

    # create collection
    if milvus_client.has_collection("HCS_Insurance"):
        milvus_client.drop_collection("HCS_Insurance")

    milvus_client.create_collection(
        collection_name="HCS_Insurance", 
        dimension=384,
        metric_type="IP",
        index_type="IVF_FLAT",
    )

    # prepare documents
    print("Preparing documents...")
    docs = []

    for file_path in glob("./documents/*.txt", recursive=True):
        with open(file_path, "r") as file:
            file_text = file.read()
            docs.append(file_text)
    vectors = model.encode(docs)

    data = [
        {"id": i, "vector": vectors[i], "text": docs[i], "subject": "insurance"}
        for i in range(len(vectors))
    ]

    # insert data
    print("Inserting data...")
    res = milvus_client.insert(collection_name="HCS_Insurance", data=data)
    print(milvus_client.describe_collection("HCS_Insurance"))
    print(res)

    return {"response": "Data prepared successfully"}



class SearchRequest(BaseModel):
    query: str
    top_k: int = 6
    relevance_threshold: float = 0.5

@app.post("/search/")
async def search_text(request: SearchRequest):
    milvus_client = MilvusClient(
        uri=milvus_uri,
        port="19530",
    )

    query_embedding = model.encode([request.query])

    search_params = {
        "metric_type": "IP", # Inner Product, a way of measuring similarity
        "params": {
            "radius": request.relevance_threshold # Only return documents relevant to the query
        }
    }

    result = milvus_client.search(
        collection_name="HCS_Insurance", 
        data=query_embedding,
        limit=request.top_k,
        search_params=search_params,
        output_fields=["text"]
    )

    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8080)