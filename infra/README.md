# infra

This folder contains Terraform scripts for provisioning infrastructure used by this project.

Structure
- main.tf       - Terraform configuration (skeleton/example)
- variables.tf  - declared variables

Notes
- Do not check in .tfstate files; they are ignored by .gitignore.
- Add backend configuration (S3, GCS, etc.) and provider credentials as needed in a secure way.