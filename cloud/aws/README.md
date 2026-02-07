# AWS Cloud Storage Module

## Purpose
This module represents the Amazon Web Services (AWS) storage backend used in the proposed multi-cloud architecture.

## Storage Service
- Amazon S3 (Object Storage)

## Stored Data
- Encrypted files only (`.enc`)
- No plaintext files
- No AES keys
- No biometric data

## Security Properties
- Data is encrypted using AES-256 before upload
- AES key is protected using Post-Quantum Key Encapsulation (ML-KEM)
- Integrity and ownership are verified via PQC digital signatures stored in the ledger

## Implementation Status
- Storage client interface implemented
- Can be configured using AWS S3 credentials
- Used for replication experiments and performance evaluation

## Notes
This module is designed to be interchangeable with other cloud providers
(Azure Blob Storage and Google Cloud Storage) to demonstrate multi-cloud
redundancy and vendor independence.

