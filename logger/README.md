# Stageopdracht HCS-Company. Onderzoek naar Retrieval Augmented Generation
Deze Stageopdracht wordt uitgevoerd voor HCS-Company om uit te zoeken wat de voordelen van RAG zijn. Dit wordt gedaan aan de hand van een demonstratie. 
Bij gebruik van dit project is gebruik gemaakt van Red Hat Openshift developer sandbox om alle applicaties te hosten. Door gebrek aan resources wordt de LLM app lokaal gehost en beschikbaar gesteld met Ngrok.

## Mappen Structuur
 - **backend**: alle code van de backend API, verwerkt de data die de frontend gebruikt. Communiceerd met Postgres database en Minio storage. Geschreven in python Flask.
 - **diagrams**: bevat alle diagrammen die vooraf gemaakt zijn voor het project.
 - **figma_design**: bevat het ontwerp gemaakt voor het frontend, gemaakt in Figma.
 - **frontend**: de demostratie website geschreven in VueJs.
 - **llm_app**: de llm applicatie bevat de AI en een API om er mee te communiceren. Dit is de enige applicatie die niet op het Openshift platform gehost worden.
 - **milvus_api**: API om te communiceren met de milvus vector database.
 - **sql_db**: PostgreSQL database om gebruikers en auto gegevens in op te slaan.
 - **vectordb**: Milvus database waar alle documenten als embeddings worden opgeslagen.