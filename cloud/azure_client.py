# cloud/azure_client.py

import os
import shutil

AZURE_CONTAINER = "results/azure"

def upload(file_path: str):
    os.makedirs(AZURE_CONTAINER, exist_ok=True)
    shutil.copy(file_path, AZURE_CONTAINER)
    print(f"[Azure] Uploaded {file_path}")

def download(file_name: str, dest: str):
    shutil.copy(os.path.join(AZURE_CONTAINER, file_name), dest)
    print(f"[Azure] Downloaded {file_name}")

def delete(file_name: str):
    os.remove(os.path.join(AZURE_CONTAINER, file_name))
    print(f"[Azure] Deleted {file_name}")

