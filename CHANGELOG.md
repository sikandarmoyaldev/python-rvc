# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.0.3] - 2026-08-18

### Fixed
- Resolved FileNotFoundError for `i18n` locale files by using absolute paths based on `__file__`, allowing the CLI to execute correctly from any working directory.

## [0.0.2] - 2026-08-18

### Added
- Included `src/tools` directory in the package build targets to resolve missing module dependencies during inference.
- Added `hf-xet` to dependencies to enable optimized, high-speed downloads for large Hugging Face model files, preventing read timeouts.

### Changed
- Updated [tool.hatch.build.targets.wheel] in pyproject.toml to explicitly package `src/tools`.
- Updated [tool.ruff] exclusions to ignore `src/tools`, preventing linting errors on copied third-party code.

### Fixed
- Resolved ModuleNotFoundError: No module named 'tools' that occurred when infer.cli attempted to import tools.cuda_graph.
- Fixed large file download timeouts (e.g., pytorch_model.bin) by enforcing Xet storage via hf-xet.

## [0.0.1] - 2026-08-18

### Added
- Initial release of the lightweight, WebUI-free RVC inference engine.
- Programmatic RVCConverter class and download_base_models utility.
- Automated Hugging Face base model downloading (HuBERT, RMVPE, pretrained v2).
- PyPI Trusted Publishing workflow via GitHub Actions.
