import tempfile
from pathlib import Path

from rvc import download_base_models


class TestModelDownload:
    def test_download_base_models_creates_directories(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            assets_dir = Path(temp_dir) / "assets"
            download_base_models(assets_dir)

            assert (assets_dir / "hubert_base").exists()
            assert (assets_dir / "rmvpe").exists()
            assert (assets_dir / "pretrained_v2").exists()
            assert (assets_dir / "weights").exists()
            assert (assets_dir / "indices").exists()
