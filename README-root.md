# weathergov-automation

A small project to interact with the Weather.gov API and hold infrastructure (Terraform) and CI workflows.

Summary
- src/               — Weather.gov API client and related code
- infra/             — Terraform scripts and infrastructure configuration
- .github/workflows/ — GitHub Actions workflows for CI (formatting, checks, tests)

Quickstart (create using GitHub web UI)
1. Use "Add file → Create new file" and name the file `README.md` at the repository root.
2. Paste the contents of this file and commit to `main` (or create a branch & PR).
3. After the README is created, add `.gitignore`, `src/` files, and `.github/workflows/ci.yml` with the same web UI or the web editor (press `.` to open).

Development notes
- Do not commit Terraform state files (.tfstate). Add them to .gitignore.
- Include a proper User-Agent header (with contact info) when calling the Weather.gov API per their policy.
- Keep any provider credentials or API keys out of the repository; use GitHub Secrets for CI.

Recommended commit and branch naming
- Commit message: Add root README.md
- Branch (if using a PR): docs/readme or feat/readme

Contact
- Owner: @raytekletics27
- For API usage, include an email or other contact in the User-Agent string in code.

License
- Add a LICENSE file if you want an explicit license. If unsure, add an SPDX header here and create LICENSE later.
