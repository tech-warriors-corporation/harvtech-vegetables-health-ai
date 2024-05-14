import os
from dataclasses import dataclass, field
from pathlib import Path
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


def get_path_to_saved_models(file_name: str):
    base_path = Path(__file__).parent

    return base_path / "weights" / file_name


class SecureRepr:
    def __repr__(self):
        return f"<{self.__class__.__name__}: sensitive content>"


@dataclass(frozen=True, order=True, repr=False)
class ModelsConstants(SecureRepr):
    available_models: set[str] = field(default_factory=lambda: {"bean_leaf", "potato_leaf", "tomato_leaf", "rice_leaf"})
    bean_leaf_weights_path = get_path_to_saved_models("best_bean_leaf.pth")
    potato_leaf_weights_path = get_path_to_saved_models("best_potato_leaf.h5")
    tomato_leaf_weights_path = get_path_to_saved_models("best_tomato_leaf_inceptionV3_256.h5")
    rice_leaf_weights_path = get_path_to_saved_models("best_rice_leaf.h5")


@dataclass(frozen=True, order=True, repr=False)
class SecurityConstants(SecureRepr):
    cloud_storage_url_prefix: str = os.getenv("cloud_storage_url_prefix")
    flask_port: int = os.getenv("flask_port")


@dataclass(frozen=True, order=True, repr=False)
class GeminiConstants(SecureRepr):
    gemini_api_key: str = os.getenv("gemini_api_key")
    threshold: int = 10
    max_attempts: int = 5
    delay_seconds: int = 1
    prompt_examples: str = Path(__file__).parent / "gemini_prompt_examples.txt"
    chunk_size: int = 1024


models_constants_instance = ModelsConstants()
security_constants_instance = SecurityConstants()
gemini_constants_instance = GeminiConstants()
