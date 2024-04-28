from dataclasses import dataclass
from pathlib import Path

@dataclass (frozen=True)
class DataIngestionConfig:
    root_dir: Path
    local_data_file: Path
    unzip_dir: Path


@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path: Path
    update_base_model_path: Path
    params_image_size: list
    params_include_top: bool
    params_classes: int
    params_weights: str
    params_learning_rate: float


@dataclass(frozen=True)
class PrepareCallbacksConfig:
    root_dir : Path
    tensorboard_root_log_dir : Path
    checkpoint_model_filepath : Path