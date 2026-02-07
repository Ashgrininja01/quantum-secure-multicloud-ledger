
# cloud/storage_client.py

from cloud.aws_client import upload as aws_upload
from cloud.azure_client import upload as azure_upload
from cloud.gcp_client import upload as gcp_upload

def replicate(file_path: str):
    """
    Replicates encrypted files across multiple clouds
    """
    aws_upload(file_path)
    azure_upload(file_path)
    gcp_upload(file_path)

    print("[Multi-Cloud] Replication completed")
