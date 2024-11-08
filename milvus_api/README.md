# milvus_api
Deze map bevat de python scripts en de Containerfile om een API te maken die met de Milvus vector database kan samenwerken. De API heeft een Persistent Volume Claim (PVC) nodig om het transformers model in op te slaan. 
De API bevat endpoints om vector search te doen op basis van een query of om alle documenten in 1x op te halen.

## Endpoints
- **/prepare/** laad alle documenten in als vectoren
- **/search/** zoek relevante documenten op, op basis van een query
- **/load-minio/** laad alle documenten in de minio opslag
- **/documents/** haal alle documenten uit minio op