from pymilvus import MilvusClient, Collection
from sentence_transformers import SentenceTransformer
from glob import glob

milvus_client = MilvusClient(host='localhost', port='19530')

if milvus_client.has_collection("demo_collection"):
    milvus_client.drop_collection("demo_collection")

milvus_client.create_collection(collection_name="demo_collection", dimension=384)

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
    {"id": i, "vector": vectors[i], "text": docs[i], "subject": "history"}
    for i in range(len(vectors))
]

# insert data
print("Inserting data...")
milvus_client.insert(collection_name="demo_collection", data=data)

print("printing complete collection...")
collection = Collection("demo_collection")
result = collection.query(expr="id >= 0")
print(result)