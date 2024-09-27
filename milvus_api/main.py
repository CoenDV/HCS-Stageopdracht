from pymilvus import MilvusClient
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

app.milvus_client = MilvusClient(
    uri='http://172.30.100.242',
    port='19530'
)

app.sentence_model = SentenceTransformer('all-MiniLM-L6-v2', cache_folder='/app/.cache')

@app.post("/prepare/")
async def generate_text():
    # create collection
    if app.milvus_client.has_collection("demo_collection"):
        app.milvus_client.drop_collection("demo_collection")

    app.milvus_client.create_collection(
        collection_name="demo_collection", 
        dimension=384,
        metric_type="IP",
        index_type="IVF_FLAT",
    )

    # prepare documents
    print("Preparing documents...")
    docs = []
    vectors = []

    for file_path in glob("./../vectordb/documents/*.txt", recursive=True):
        with open(file_path, "r") as file:
            file_text = file.read()
            docs.append(file_text)
            vectors.append(app.model.encode(file_text))

    data = [
        {"id": i, "vector": vectors[i], "text": docs[i], "subject": "insurance"}
        for i in range(len(vectors))
    ]

    # insert data
    print("Inserting data...")
    res = app.milvus_client.insert(collection_name="demo_collection", data=data)
    print(app.milvus_client.describe_collection("demo_collection"))
    print(res)

    return {"response": "Data prepared successfully"}

@app.post("/search/")
async def search_text(query, top_k=6, relevance_threshold=0.5):
    query_embedding = app.sentence_model.encode([query])

    search_params = {
        "metric_type": "IP", # Inner Product, a way of measuring similarity
        "params": {
            "radius": relevance_threshold # Only return documents relevant to the query
        }
    }

    result = app.milvus_client.search(
        collection_name="demo_collection", 
        data=query_embedding,
        limit=top_k,
        search_params=search_params,
        output_fields=["text"]
    )

    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8080)