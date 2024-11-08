# Vectordb
Deze map bevat alle onderdelen om de milvus vecor database te deployen op Openshift. De 3 YAML files creëren ieder een pod die iets regelt voor de database.
- **etcd**: bewaard de key-value pairs van de database. Slaat ook verschillende configuratie bestanden op.
- **minio**: is een bucket storage die gebruikt wordt om de context documenten op te slaan
- **milvus-standalone**: het hoofd component, beheerd de 2 andere pods. Standalone betekent dat het in 1 pod gehost wordt en zich niet probeert te verspreiden over een cluster.

Per component wordt er een Persistent Volume Chain (PVC) gemaakt om de data op te slaan.