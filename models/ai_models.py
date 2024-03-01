import os

os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

from abc import ABC, abstractmethod
import tensorflow as tf
import torch
from PIL import Image
from torchvision import models, transforms
from torchvision.transforms import v2
from constants.ModelsConstants import ModelsConstants
from tensorflow.keras.preprocessing import image
import numpy as np
from logs.log_config import configure_logger

logger = configure_logger(__name__)
models_constant = ModelsConstants()


class IAModel(ABC):
    @abstractmethod
    def predict(self, image_content):
        pass


class TomatoLeafModel(IAModel):
    def __init__(self):
        self.__load_model()
        self.class_names = ["Bacterial_spot", "Early_blight", "Late_blight", "Leaf_Mold", "Septoria_leaf_spot",
                            "Spider_mites Two-spotted_spider_mite", "Target_Spot", "Tomato_Yellow_Leaf_Curl_Virus",
                            "Tomato_mosaic_virus", "healthy"]

    def __load_model(self):
        self.model = tf.keras.models.load_model(ModelsConstants.tomato_leaf_weights_path)

    def predict(self, image_content):
        img = image.load_img(image_content, target_size=(256, 256))
        img_array = image.img_to_array(img)
        img_array_rescaled = img_array / 255.0
        prepared_image = np.expand_dims(img_array_rescaled, axis=0)
        prediction = self.model.predict(prepared_image)[0]
        probabilities_dict = {class_name: float(probability) * 100 for class_name, probability in
                              zip(self.class_names, prediction)}

        return {
            "predicted": {
                "class": self.class_names[np.argmax(prediction)],
                "confidence": np.max(prediction) * 100
            },
            "probabilities_dict": probabilities_dict
        }


class PotatoLeafModel(IAModel):
    def __init__(self):
        self.__load_model()
        self.class_names = ["Early_Blight", "Healthy", "Late_Blight"]

    def __load_model(self):
        self.model = tf.keras.models.load_model(ModelsConstants.potato_leaf_weights_path)

    def predict(self, image_content):
        img = image.load_img(image_content, target_size=(256, 256))
        img_array = image.img_to_array(img)
        prepared_image = np.expand_dims(img_array, axis=0)
        prediction = self.model.predict(prepared_image)[0]
        probabilities_dict = {class_name: float(probability) * 100 for class_name, probability in
                              zip(self.class_names, prediction)}

        return {
            "predicted": {
                "class": self.class_names[np.argmax(prediction)],
                "confidence": np.max(prediction) * 100
            },
            "probabilities_dict": probabilities_dict
        }


class BeanLeafModel(IAModel):
    def __init__(self):
        self.__get_device_type()
        self.__initialize_model()
        self._transform = self.__set_transform()
        self.class_names = ["healthy", "angular_leaf_spot", "bean_rust"]

    def __get_device_type(self):
        logger.info(f"CUDA available: {torch.cuda.is_available()}")
        self.device = torch.device(
            "cuda" if torch.cuda.is_available() else "cpu")

    def __set_transform(self):
        return transforms.Compose([
            v2.Resize((224, 224)),
            v2.PILToTensor(),
            v2.ToDtype(torch.float32),
            v2.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ])

    def __initialize_model(self):
        self.model = models.efficientnet_v2_s(weights=None)
        self.model.classifier[1] = torch.nn.Linear(1280, 3)
        self.model.load_state_dict(torch.load(ModelsConstants.bean_leaf_weights_path, map_location=self.device))
        self.model = self.model.to(self.device)
        self.model.eval()

    def predict(self, image_content):
        image = Image.open(image_content)
        image = self._transform(image).unsqueeze(0)
        image = image.to(self.device)

        with torch.no_grad():
            outputs = self.model(image)
            probabilities = torch.nn.functional.softmax(outputs, dim=1)
            confidence, predicted = torch.max(probabilities, 1)

        probabilities_dict = {class_name: probability.item() * 100 for class_name, probability in
                              zip(self.class_names, probabilities[0])}

        return {
            "predicted": {
                "class": self.class_names[predicted],
                "confidence": confidence.item() * 100
            },
            "probabilities_dict": probabilities_dict
        }
