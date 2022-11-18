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
from azure.storage.blob import BlobServiceClient
from typing import List
from typing import Tuple

def main(container: str) -> List[Tuple[int, str]]:
    
    connect_str=os.getenv('AZURE_STORAGE_CONNECTION_STRING')

    blob_service_client=BlobServiceClient.from_connection_string(connect_str)

    container_client=blob_service_client.get_container_client(container=container)

    blob_list=container_client.list_blobs()

    pairs=[]

    for blob in blob_list:
        file=container_client.download_blob(blob.name).content_as_text()

        lines=file.splitlines()
        line_numbers=list(range(1, len(lines)+1))
        pairs=pairs+list(zip(line_numbers, lines))
    
    return pairs

   