```text
# weathergov-automation

A small project to interact with the Weather.gov API and hold infrastructure (Terraform) and CI workflows.

Summary
- src/               — Weather.gov API client and related code
- infra/             — Terraform scripts and infrastructure configuration
- .github/workflows/ — GitHub Actions workflows for CI (formatting, checks, tests)

Quickstart
1. Clone the repo or use the GitHub web UI to add files.
2. Add these directories/files:
   - infra/ (Terraform files: main.tf, variables.tf, etc.)
   - src/ (Python code, e.g., src/weather_client.py)
   - .github/workflows/ (CI workflows, e.g., ci.yml)
   - .gitignore and requirements.txt before committing local changes.
3. Prefer making changes on a branch and opening a pull request for review.

Development notes
- Do not commit Terraform state files (.tfstate); add them to .gitignore.
- Include a proper User-Agent header (with contact info) when calling the Weather.gov API per their policy.
- Keep provider credentials or API keys out of the repository; use GitHub Secrets for CI.
- Add a LICENSE file if you want to specify usage terms.

Suggested commit and branch
- Commit message: Update README.md
- Branch name (if using a PR): docs/readme

Contact
- Owner: @raytekletics27
- For API usage, include an email or other contact in the User-Agent string in code.
```
