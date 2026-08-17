import os
import sys
from pathlib import Path


class RVCConverter:
    def __init__(
        self, model_path: str, assets_dir: str = "assets", device: str = "cpu"
    ):
        self.model_path = Path(model_path).resolve()
        self.assets_dir = Path(assets_dir).resolve()
        self.device = device

        if not self.model_path.exists():
            raise FileNotFoundError(f"Model not found at: {self.model_path}")

        self._setup_environment()

    def _setup_environment(self):
        os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
        os.environ.setdefault("weight_root", str(self.assets_dir / "weights"))
        os.environ.setdefault("index_root", str(self.assets_dir.parent / "logs"))
        os.environ.setdefault("outside_index_root", str(self.assets_dir / "indices"))
        os.environ.setdefault("rmvpe_root", str(self.assets_dir / "rmvpe"))

        package_root = Path(__file__).resolve().parent.parent
        if str(package_root) not in sys.path:
            sys.path.insert(0, str(package_root))

    def convert(
        self,
        input_path: str,
        output_path: str | None = None,
        pitch: int = 0,
        f0_method: str = "rmvpe",
        index_rate: float = 0.0,
        protect: float = 0.33,
        rms_mix_rate: float = 1.0,
    ) -> str:
        from infer.cli import main as rvc_main_cli

        input_p = Path(input_path).resolve()

        if output_path is None:
            output_dir = self.assets_dir.parent / "output"
            output_dir.mkdir(parents=True, exist_ok=True)
            output_p = output_dir / input_p.name
        else:
            output_p = Path(output_path).resolve()
            if output_p.is_dir():
                output_p = output_p / input_p.name

        sys.argv = [
            "rvc",
            "--model",
            str(self.model_path),
            "--input",
            str(input_p),
            "--output",
            str(output_p),
            "--pitch",
            str(pitch),
            "--f0-method",
            f0_method,
            "--index-rate",
            str(index_rate),
            "--protect",
            str(protect),
            "--rms-mix-rate",
            str(rms_mix_rate),
            "--overwrite",
        ]

        print(f"Converting: {input_p.name} -> {output_p.name}")

        exit_code = rvc_main_cli()

        if exit_code != 0:
            raise RuntimeError(f"RVC conversion failed with exit code {exit_code}")

        return str(output_p)
