# API Versioning Strategy

ForgeMind uses URL-based API versioning.

## Current Version

v1

Example:

GET /api/v1/assets/

## Future Versions

Breaking changes will introduce a new version:

GET /api/v2/assets/

## Rules

- Existing versions remain backward compatible.
- Breaking changes require a new API version.
- Deprecated versions will be announced before removal.