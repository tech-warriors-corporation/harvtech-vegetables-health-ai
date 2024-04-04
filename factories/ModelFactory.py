from models.ai_models import BeanLeafModel, PotatoLeafModel, TomatoLeafModel, RiceLeafModel


class ModelFactory:
    model_registry = {
        "bean_leaf": BeanLeafModel,
        "potato_leaf": PotatoLeafModel,
        "tomato_leaf": TomatoLeafModel,
        "rice_leaf": RiceLeafModel
    }

    @staticmethod
    def get_model(model_type):
        try:
            model_class = ModelFactory.model_registry[model_type]

            return model_class()
        except KeyError:
            raise ValueError(f"Model type \"{model_type}\" not supported")
