# cloud/aws_client.py

import os
import shutil

AWS_BUCKET = "results/aws"

def upload(file_path: str):
    os.makedirs(AWS_BUCKET, exist_ok=True)
    shutil.copy(file_path, AWS_BUCKET)
    print(f"[AWS] Uploaded {file_path} to AWS bucket")

def download(file_name: str, dest: str):
    src = os.path.join(AWS_BUCKET, file_name)
    shutil.copy(src, dest)
    print(f"[AWS] Downloaded {file_name} from AWS")

def delete(file_name: str):
    os.remove(os.path.join(AWS_BUCKET, file_name))
    print(f"[AWS] Deleted {file_name}")

