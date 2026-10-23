# Security Scanning

## Purpose

Security scanning helps identify vulnerabilities in application code, dependencies, container images, and running web applications before release.

## Security Checks

* **Secret Scanning:** Detects accidentally exposed credentials and secrets.
* **Static Application Security Testing (SAST):** Analyses source code for potential security weaknesses.
* **Dependency Scanning:** Checks project dependencies for known vulnerabilities.
* **Container Image Scanning:** Identifies known vulnerabilities in container images.
* **Dynamic Application Security Testing (DAST):** Tests a running application for potential web security issues using tools such as OWASP ZAP.

## Pipeline Integration

Security checks should run at the appropriate stages of the CI/CD workflow. Critical findings should prevent release promotion according to the project's configured security policy.

## Verification

The actual workflow configuration and execution logs must be reviewed to confirm which scans run and whether they pass or fail.
