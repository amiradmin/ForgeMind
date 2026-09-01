# Security Policy

## Reporting a vulnerability

Please do not report security vulnerabilities in a public issue.

Use the private security reporting option on GitHub when it is available. If private vulnerability reporting is not available, contact the maintainer through the professional contact method listed on the maintainer's GitHub profile and include:

- A clear description of the issue
- Affected component and version or commit
- Reproduction steps or proof of concept
- Expected security impact
- Any suggested remediation

Do not include real credentials, production data, proprietary industrial data, or personal information.

## Scope

Security-sensitive areas include:

- Authentication and JWT handling
- Authorization, RBAC, and tenant isolation
- Secret and environment configuration
- API input validation
- File and data ingestion
- Celery tasks and message handling
- Dependency and container security
- Audit logs and sensitive operational data
- AI provider integrations and model-input boundaries

## Coordinated disclosure

Please allow reasonable time for investigation and remediation before public disclosure. Good-faith security research and responsible reporting are welcome.
