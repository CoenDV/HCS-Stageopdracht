from minio import Minio
from models import Document
import glob
import os

class minio_utils:

    def __init__(self, uri, access_key, secret_key):
        self.minio_client = Minio(
            endpoint=uri,
            access_key=access_key,
            secret_key=secret_key,
            secure=False,
        )

        self.bucket_name = "insurancedocuments"

    # https://stackoverflow.com/questions/66136763/how-to-upload-a-directory-to-minio-using-python
    def load_documents(self):
        source_directory = "./documents/"

        # Make the bucket if it doesn't exist.
        found = self.minio_client.bucket_exists(self.bucket_name)
        if not found:
            self.minio_client.make_bucket(self.bucket_name)
            print("Created bucket", self.bucket_name)
        else:
            print("Bucket", self.bucket_name, "already exists")

        # Upload all documents in the source_directory to the bucket
        for local_file in glob.glob(source_directory + "**"):
            local_file = local_file.replace(os.sep, "/")                                # Replace \ with / on Windows
            object_name = local_file[len(source_directory):]                            # Remove the source_directory from the filename
            self.minio_client.fput_object(self.bucket_name, object_name, local_file)    # Upload the file to the bucket
            print("Uploading", local_file, "to", self.bucket_name)

        return {"response": "Documents loaded successfully"}

    
    def get_documents(self):
        objects = self.minio_client.list_objects(self.bucket_name)

        response = []
        for object in objects:
            print(object)
            response.append(Document(
                object.etag,
                object.object_name,
                self.minio_client.get_object(self.bucket_name, object.object_name).data.decode("utf-8")
            ))

        print(response)
        return response