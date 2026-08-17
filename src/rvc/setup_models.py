import os
from pathlib import Path

from huggingface_hub import hf_hub_download


def download_base_models(assets_dir: str | Path = "assets"):
    assets_path = Path(assets_dir).resolve()

    for subdir in ["hubert_base", "rmvpe", "pretrained_v2", "weights", "indices"]:
        (assets_path / subdir).mkdir(parents=True, exist_ok=True)

    downloads = [
        ("hubert_base/config.json", "assets"),
        ("hubert_base/preprocessor_config.json", "assets"),
        ("hubert_base/pytorch_model.bin", "assets"),
        ("rmvpe.pt", "assets/rmvpe"),
        ("pretrained_v2/f0D40k.pth", "assets"),
        ("pretrained_v2/f0G40k.pth", "assets"),
    ]

    print("Checking and downloading base RVC models...")
    for filename, local_dir in downloads:
        final_path = assets_path / local_dir / os.path.basename(filename)
        if not final_path.exists():
            print(f"Downloading {filename} ...")
            hf_hub_download(
                repo_id="lj1995/VoiceConversionWebUI",
                filename=filename,
                local_dir=str(assets_path),
            )
        else:
            print(f"Already exists: {os.path.basename(filename)}")

    print("Base models ready.")
