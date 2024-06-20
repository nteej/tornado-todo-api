# Changelog

## [Unreleased]

## [1.0.1] - 2024-06-20
### Added
- Introduced CI/CD best practices for a Debian server using GitHub.
- Added comprehensive unit tests with edge cases and validation error handling.

### Changed
- Decoupled the model for improved performance.
- API response now managed using transformers for a more decoupled architecture.

### Fixed
- Corrected the issue with the `test_create_todo` failing due to a TypeError.
- Resolved `FAILED test_app.py::TodoTest::test_get_todos - AssertionError`.

## [1.0.0] - 2024-06-15
### Added
- Created the initial Todo API using Tornado.
- Implemented full CRUD operations for the Todo API.
- Added validation handling in separate request classes.
- Introduced exception handling for API responses.