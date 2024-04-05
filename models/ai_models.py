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
import albumentations as albu
import cv2
from logs.log_config import configure_logger

logger = configure_logger(__name__)
models_constant = ModelsConstants()


class IAModel(ABC):
    @abstractmethod
    def predict(self, image_content):
        pass

    def tensorflow_return(self, prediction, class_names):
        max_probability_index = np.argmax(prediction)
        return {
            "predicted": {
                "class": class_names[max_probability_index],
                "confidence": prediction[max_probability_index] * 100
            },
            "probabilities_dict": {class_name: float(prob) * 100 for class_name, prob in zip(class_names, prediction)}
        }

    def torch_return(self, outputs, predicted_index, class_names):
        probabilities = torch.nn.functional.softmax(outputs, dim=1)
        max_probability = probabilities[0][predicted_index].item()
        return {
            "predicted": {
                "class": class_names[predicted_index],
                "confidence": max_probability * 100
            },
            "probabilities_dict": {
                class_name: prob.item() * 100 for class_name, prob in zip(class_names, probabilities[0])}
        }


class RiceLeafModel(IAModel):
    def __init__(self):
        self.__load_model()
        self.aug_types = self.__set_augmentation()
        self.class_names = ['bacterial_leaf_blight', 'brown_spot', 'leaf_smut']

    def __load_model(self):
        self.model = tf.keras.models.load_model(ModelsConstants.rice_leaf_weights_path)

    def __set_augmentation(self):
        return albu.Compose([
            albu.HorizontalFlip(),
            albu.OneOf([
                albu.HorizontalFlip(),
                albu.VerticalFlip(),
            ], p=0.8),
            albu.OneOf([
                albu.RandomContrast(),
                albu.RandomGamma(),
                albu.RandomBrightness(),
            ], p=0.3),
            albu.OneOf([
                albu.ElasticTransform(alpha=120, sigma=120 * 0.05, alpha_affine=120 * 0.03),
                albu.GridDistortion(),
                albu.OpticalDistortion(distort_limit=2, shift_limit=0.5),
            ], p=0.3),
            albu.ShiftScaleRotate()
        ])

    def __preprocess_image(self, image_content):
        image_bytes = np.asarray(bytearray(image_content.read()), dtype=np.uint8)
        image = cv2.imdecode(image_bytes, cv2.IMREAD_COLOR)

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = cv2.resize(image, (224, 224))

        augmented = self.aug_types(image=image)
        image = augmented['image']

        return image / 255.0

    def predict(self, image_content):
        image = self.__preprocess_image(image_content)
        prepared_image = np.expand_dims(image, axis=0)
        prediction = self.model.predict(prepared_image)[0]
        return self.tensorflow_return(prediction, self.class_names)


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
        return self.tensorflow_return(prediction, self.class_names)


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
        return self.tensorflow_return(prediction, self.class_names)


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
            _, predicted = torch.max(outputs, 1)

        return self.torch_return(outputs, predicted, self.class_names)
