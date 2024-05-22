from lib.models.base_model import BaseModel
from lib.vulnerabilites.vulnerability import Vulnerability

class Analysis:
    def __init__(self, model_used: BaseModel, vulnerabilites: list[Vulnerability], analyzed_code, message: str | None = None) -> None:
        self.model_used = model_used
        self.vulnerabilites = vulnerabilites
        self.analyzed_code = analyzed_code
        self.message = message

    def toDict(self):
        return {
            'model_used': self.model_used.toDict(),
            'vulnerabilities': [v.toDict() for v in self.vulnerabilites],
            'analyzed_code': self.analyzed_code,
            'message': self.message
        }
