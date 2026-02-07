# Azure Cloud Storage Module

## Purpose
This module represents Microsoft Azure as a storage provider in the
multi-cloud encrypted storage system.

## Storage Service
- Azure Blob Storage

## Stored Data
- AES-256 encrypted files only
- No cryptographic keys or biometric information

## Security Model
- End-to-end encryption is applied before cloud upload
- Azure acts as an untrusted storage provider
- Integrity verification is performed using PQC signatures and ledger records

## Implementation Status
- Storage abstraction layer defined
- Supports replication alongside AWS and GCP

## Notes
Azure is used to evaluate redundancy, availability, and resilience
in the proposed multi-cloud architecture.

