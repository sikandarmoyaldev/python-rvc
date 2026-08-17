# sikandarmoyaldev-rvc

Lightweight, WebUI-free RVC (Retrieval-based Voice Conversion) inference engine for the python project.

## 📦 Installation

```bash
pip install sikandarmoyaldev-rvc
# or
pip install git+https://github.com/sikandarmoyaldev/python-rvc.git
```

## 📖 Usage

### 1. Download Base Models

Before converting, you must download the required base models (`HuBERT`, `RMVPE`, etc.).

```python
from rvc import download_base_models

download_base_models("assets")
```

### 2. Convert Audio

Initialize the converter with your custom `.pth` model and convert your audio files.

```python
from rvc import RVCConverter

# Initialize with your model path and assets directory
converter = RVCConverter(model_path="alex.pth", assets_dir="assets")

# Convert a single file (output defaults to "output/input_filename.wav")
output_file = converter.convert(
    input_path="group-1.wav", pitch=2, f0_method="rmvpe", index_rate=0.0
)

print(f"Saved to: {output_file}")
```

## 🚀 Development

This project uses `uv` for dependency management.

```bash
# Install dependencies
uv sync

# Format and lint code
uv run ruff format .
uv run ruff check . --fix
```
