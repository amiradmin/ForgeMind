# Contributing to ForgeMind

Thank you for your interest in ForgeMind. Contributions from industrial engineers, backend developers, data engineers, ML engineers, researchers, technical writers, and product thinkers are welcome.

## Ways to contribute

- Improve Django or Django REST Framework modules
- Design industrial asset, maintenance, telemetry, and reliability domains
- Build Predictive Maintenance, anomaly-detection, or RUL baselines
- Add Computer Vision use cases for industrial operations
- Improve tests, documentation, API examples, and developer experience
- Review architecture decisions and propose industrial use cases
- Translate selected documentation, including Persian documentation

## Before starting

1. Read the [README](README.md) and open issues.
2. For a substantial change, open an issue first so we can agree on scope and design.
3. Look for focused issues that can be completed and reviewed independently.
4. Never include proprietary plant data, credentials, personal data, or employer/client material.

## Development workflow

1. Fork the repository.
2. Create a focused branch from `main`.
3. Add or update tests for behavioral changes.
4. Run the relevant quality checks.
5. Open a pull request using the repository template.

Keep changes small, documented, and easy to review.

## Engineering expectations

- Follow the existing modular and domain-first architecture.
- Keep business rules out of transport-layer code.
- Preserve organization and tenant boundaries.
- Add type hints and useful docstrings where they improve clarity.
- Use environment variables for configuration and never commit secrets.
- Document important architectural trade-offs.
- Prefer explainable, measurable AI behavior over opaque demos.

## Pull requests

A good pull request:

- Links to a related issue
- Explains the problem and the chosen approach
- Lists tests performed
- Notes migrations, API changes, and compatibility implications
- Updates documentation when behavior changes

## Communication

Use GitHub Issues for actionable work and bug reports. Use GitHub Discussions for questions, ideas, architecture conversations, introductions, and collaboration proposals.

You can write in English or Persian. English is preferred for shared technical documentation so the widest community can participate.

## Recognition

Contributors are credited through Git history, pull requests, releases, and project acknowledgements. Meaningful contributors may be invited to take broader ownership of a module.

By participating, you agree to follow the [Code of Conduct](CODE_OF_CONDUCT.md).
