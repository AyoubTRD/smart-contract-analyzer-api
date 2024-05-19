from lib.models.base_model import BaseModel
from lib.analysis.analysis import Analysis
from lib.vulnerabilites.vulnerability import Vulnerability

class LSTMModel(BaseModel):
    def __init__(self) -> None:
        super().__init__(id='lstm', name='LSTM', desc='LSTM description', supports_sourcecode=True)

    def analyze(self, code) -> Analysis:
        is_sourcecode = True

        if not is_sourcecode:
            raise Exception('LSTMModel only supports Source Code')

        vulnerabilites = [
            Vulnerability("1", "Vulnerability 1", "Vulnerability 1"),
            Vulnerability("2", "Vulnerability 2", "Vulnerability 2"),
            Vulnerability("3", "Vulnerability 3", "Vulnerability 3"),
        ]
        return Analysis(model_used=self, analyzed_code=code, vulnerabilites=vulnerabilites)
