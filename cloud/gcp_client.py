
# cloud/gcp_client.py

import os
import shutil

GCP_BUCKET = "results/gcp"

def upload(file_path: str):
    os.makedirs(GCP_BUCKET, exist_ok=True)
    shutil.copy(file_path, GCP_BUCKET)
    print(f"[GCP] Uploaded {file_path}")

def download(file_name: str, dest: str):
    shutil.copy(os.path.join(GCP_BUCKET, file_name), dest)
    print(f"[GCP] Downloaded {file_name}")

def delete(file_name: str):
    os.remove(os.path.join(GCP_BUCKET, file_name))
    print(f"[GCP] Deleted {file_name}")
