from lib.models.base_model import BaseModel

class BLSTMModel(BaseModel):
    def __init__(self) -> None:
        super().__init__(id='blstm', name='BLSTM', desc='BLSTM description', supports_sourcecode=True)
