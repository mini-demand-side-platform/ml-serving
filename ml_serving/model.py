import pickle
from abc import ABC, abstractmethod
from typing import List

from .logger import get_logger
from .object_storage import ObjectStorage

log = get_logger(logger_name="model")


class Model(ABC):
    @abstractmethod
    def predict(self):
        pass

    @abstractmethod
    def get_latest_model(self):
        pass


class SklearnModel(Model):
    def __init__(self, default_ctr: float) -> None:
        self._default_ctr = default_ctr
        self._latest_model = None

    def predict(self, inputs: List[List[float]]) -> List[float]:
        if self._latest_model is None:
            return [self._default_ctr] * len(inputs)
        predicted_proba = self._latest_model.predict_proba(inputs)
        return [x[1] for x in predicted_proba]

    def get_latest_model(self, object_storage: ObjectStorage) -> None:
        model_names = object_storage.list_object("models")
        model_names.sort(reverse=True)

        if len(model_names) == 2:
            object_name = model_names[0]
        else:
            object_name = model_names[2]
        # print(sorted_model_names)
        self._latest_model = pickle.loads(
            object_storage.get_object(
                bucket_name="models", object_name=object_name
            ).read()
        )
        log.info("update model to {model_name}".format(model_name=object_name))
