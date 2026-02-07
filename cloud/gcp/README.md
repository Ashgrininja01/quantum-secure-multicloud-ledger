
# Google Cloud Storage Module

## Purpose
This module represents Google Cloud Platform (GCP) in the proposed
quantum-secure multi-cloud storage framework.

## Storage Service
- Google Cloud Storage (GCS)

## Stored Data
- Encrypted files (`.enc`)
- Metadata references only (hashes and identifiers)

## Security Properties
- Files are encrypted locally using AES-256
- Encryption keys are protected using Post-Quantum Cryptography
- Ledger ensures tamper detection and auditability

## Implementation Status
- Designed for cloud replication experiments
- Used in result analysis for availability and fault tolerance

## Notes
GCP acts as an independent cloud provider to demonstrate resistance
against single-provider failures.
