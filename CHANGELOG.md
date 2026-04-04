# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.3.0] - 2026-03-22

### Added
- Wizard Robbers character generator module (`wizard_robbers`)
- Wizard Robbers PDF character sheet generation via WeasyPrint
- DCC Dying Earth data module (occupations, weapons, animus, rations, clothing)

## [0.2.0] - 2026-03-16

### Changed
- Switched build backend from setuptools to hatchling
- Replaced black + flake8 with ruff for linting and formatting
- Replaced pip-compile requirements files with uv lockfile
- Rewrote Makefile with uv-based targets
- Updated requires-python from >=3.8 to >=3.11
- Updated .pre-commit-config.yaml to use ruff-pre-commit
- Modernized type annotations to Python 3.11+ syntax

### Added
- pytest test suite with coverage
- GitHub Actions CI workflows (test, version check, changelog check)
- CHANGELOG.md

### Removed
- ASSH (Astonishing Swordsmen & Sorcerers of Hyperborea) module
- D666 module

## [0.1.1] - 2024-01-01

### Added
- Initial release with character generators for ASSH, D666, Gamma Five, Maze Rats, and Tiny Dungeon
- Utility functions for dice rolling, ability score modifiers, and formatting
- Miscellaneous data modules (DCC occupations, Knave spells, Zothique names)

[0.3.0]: https://github.com/jderam/rpg_tools/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/jderam/rpg_tools/compare/v0.1.1...v0.2.0
[0.1.1]: https://github.com/jderam/rpg_tools/releases/tag/v0.1.1
