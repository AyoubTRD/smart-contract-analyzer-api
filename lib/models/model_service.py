from lib.models.BLSTM_model import BLSTMModel
from lib.models.CNN_model import CNNModel
from lib.models.LSTM_model import LSTMModel
from lib.models.base_model import BaseModel

class ModelService:
    models: list[BaseModel]

    def __init__(self) -> None:
        self.models = [
            CNNModel(),
            LSTMModel(),
            BLSTMModel(),
        ]

    def get_available_models(self):
        return self.models

    def get_model_by_id(self, id: str) -> BaseModel:
        for model in self.models:
            if model.id == id:
                return model

        raise Exception(f'Model with id {id} not found')

modelService = ModelService()
