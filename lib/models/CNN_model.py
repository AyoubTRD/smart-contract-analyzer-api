from lib.analysis.analysis import Analysis
from lib.models.base_model import BaseModel
from lib.vulnerabilites.vulnerability import Vulnerability

class CNNModel(BaseModel):
    def __init__(self) -> None:
        super().__init__(id='cnn', name='CNN', desc='Test', supports_bytecode=True, supports_sourcecode=False)

    def analyze(self, code) -> Analysis:
        is_bytecode = True

        if not is_bytecode:
            raise Exception('CNNModel only supports bytecode')

        vulnerabilites = [
            Vulnerability("1", "Vulnerability 1", "Vulnerability 1"),
            Vulnerability("2", "Vulnerability 2", "Vulnerability 2"),
            Vulnerability("3", "Vulnerability 3", "Vulnerability 3"),
        ]
        return Analysis(model_used=self, analyzed_code=code, vulnerabilites=vulnerabilites)
