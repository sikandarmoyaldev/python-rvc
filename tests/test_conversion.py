import os
import tempfile
from pathlib import Path

import pytest

from rvc import RVCConverter

# Resolve paths relative to the project root
PROJECT_ROOT = Path(__file__).parent.parent
MODEL_PATH_DEFAULT = PROJECT_ROOT / "assets" / "weights" / "alex.pth"
SAMPLE_AUDIO_DEFAULT = PROJECT_ROOT / "assets" / "input" / "sample.mp3"


class TestRVCConversion:
    def test_converter_raises_error_for_missing_model(self):
        with pytest.raises(FileNotFoundError):
            RVCConverter(model_path="non_existent_model.pth")

    @pytest.mark.skipif(
        not os.environ.get("RUN_INTEGRATION_TESTS"),
        reason="Integration test requires a real model and sample audio. Set RUN_INTEGRATION_TESTS=1 to run.",
    )
    def test_actual_conversion(self):
        model_path = Path(os.environ.get("TEST_MODEL_PATH", str(MODEL_PATH_DEFAULT)))
        sample_audio = Path(
            os.environ.get("TEST_SAMPLE_AUDIO", str(SAMPLE_AUDIO_DEFAULT))
        )

        if not model_path.exists():
            pytest.skip(f"Test model not found at {model_path}")
        if not sample_audio.exists():
            pytest.skip(f"Sample audio not found at {sample_audio}")

        with tempfile.TemporaryDirectory() as temp_dir:
            assets_dir = Path(temp_dir) / "assets"
            assets_dir.mkdir()

            converter = RVCConverter(
                model_path=str(model_path), assets_dir=str(assets_dir)
            )

            output_path = Path(temp_dir) / "output.wav"

            result = converter.convert(
                input_path=str(sample_audio),
                output_path=str(output_path),
                pitch=0,
                f0_method="rmvpe",
                index_rate=0.0,
            )

            assert Path(result).exists()
            assert Path(result).stat().st_size > 0
