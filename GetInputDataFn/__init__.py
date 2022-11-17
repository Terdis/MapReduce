# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import os
import uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

def main(blob_service_client: BlobServiceClient) -> str:
    
    MY_CONNECTION_STRING= "<replace>"
    MY_BLOB_CONTAINER="<replace>"

    LOCAL_BLOB_PATH="./input"
    return "HELLO"

    class AzureBlobFileDownloader:
        def __init__(self):
            print("Initializing AzureBlobFileDownloader")
        
            self.blob_service_client=BlobServiceClient.from_connection_string(MY_CONNECTION_STRING)
            self.my_container=self.blob_service_client.get_container_client(MY_BLOB_CONTAINER)

        def save_blob(self, file_name, file_content):
            download_file_path=os.path.join(LOCAL_BLOB_PATH, file_name)

            os.makedirs(os.path.dirname(download_file_path), exist_ok=True)
            with open(download_file_path, "wb") as file:
                file.write(file_content)
        
        def download_all_blobs_in_container(self):
            my_blobs=self.my_containter.list_blobs()
            for blob in my_blobs:
                print(blob.name)
                bytes=self.my_container.get_blob_client(blob).download_blob().readall()
                self.save_blob(blob.name, bytes)

    azure_blob_file_downloader=AzureBlobFileDownloader()
    azure_blob_file_downloader.download_all_blobs_in_container()