import os
from dataclasses import dataclass, field
from pathlib import Path
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


def get_path_to_saved_models(file_name: str):
    base_path = Path(__file__).parent

    return base_path / "weights" / file_name


@dataclass(frozen=True, order=True)
class ModelsConstants:
    available_models: set[str] = field(default_factory=lambda: {"bean_leaf", "potato_leaf", "tomato_leaf", "rice_leaf"})
    bean_leaf_weights_path = get_path_to_saved_models("best_bean_leaf.pth")
    potato_leaf_weights_path = get_path_to_saved_models("best_potato_leaf.h5")
    tomato_leaf_weights_path = get_path_to_saved_models("best_tomato_leaf_inceptionV3_256.h5")
    rice_leaf_weights_path = get_path_to_saved_models("best_rice_leaf.h5")
    cloud_storage_url_prefix: str = os.getenv("cloud_storage_url_prefix")
