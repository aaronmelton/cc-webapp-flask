# CHANGELOG


## [0.1.3] - 2026-04-22
### Security
- pyproject.toml: Bumped `black` to `^26.3.1` to resolve GHSA (arbitrary file writes from unsanitized user input in cache file name).
- pyproject.toml: Bumped `pytest` to `^9.0.3` to resolve GHSA (vulnerable tmpdir handling).


## [0.1.2] - 2024-09-25
### Fixed
- Somewhere along the line the file permissions got jacked up. Removed executable permissions off the files.


## [0.1.1] - 2024-09-17
### Changed
- docker-compose.yml, docker_build.sh: Fixing labels for GitHub Container Registry.


## [0.1.0] - 2023-08-02
### Added
- Beginning a new project.
