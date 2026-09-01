# Contributing to ForgeMind

Thank you for your interest in ForgeMind. Contributions from industrial engineers, backend developers, data engineers, ML engineers, researchers, technical writers, and product thinkers are welcome.

## Start here

If this is your first ForgeMind contribution, begin with the curated newcomer queue:

- [Good first issues](https://github.com/amiradmin/ForgeMind/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22good%20first%20issue%22) — small, bounded tasks suitable for learning the repository
- [Help wanted](https://github.com/amiradmin/ForgeMind/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22help%20wanted%22) — tasks where outside expertise or implementation help is especially welcome
- [GitHub Discussions](https://github.com/amiradmin/ForgeMind/discussions) — questions, introductions, architecture conversations, and collaboration ideas

To claim a focused issue, leave a short comment describing your intended approach before starting. This helps avoid duplicated work and keeps the scope reviewable.

`good first issue` means the task is intentionally limited for a newcomer. `help wanted` means outside help is welcome, but the task may require more domain or codebase knowledge.

## Ways to contribute

- Improve Django or Django REST Framework modules
- Design industrial asset, maintenance, telemetry, and reliability domains
- Build Predictive Maintenance, anomaly-detection, or RUL baselines
- Add Computer Vision use cases for industrial operations
- Improve tests, documentation, API examples, and developer experience
- Review architecture decisions and propose industrial use cases
- Translate selected documentation, including Persian documentation

## Before starting

1. Read the [README](README.md) and the relevant issue or domain documentation.
2. For a substantial change, open an issue first so scope and design can be discussed.
3. Prefer focused work that can be completed and reviewed independently.
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
- Contains no secrets, proprietary industrial data, or unrelated changes

## Communication

Use GitHub Issues for actionable work and bug reports. Use GitHub Discussions for questions, ideas, architecture conversations, introductions, and collaboration proposals.

You can write in English or Persian. English is preferred for shared technical documentation so the widest community can participate.

## Recognition

Contributors are credited through Git history, pull requests, releases, and project acknowledgements. Meaningful contributors may be invited to take broader ownership of a module.

By participating, you agree to follow the [Code of Conduct](CODE_OF_CONDUCT.md).
