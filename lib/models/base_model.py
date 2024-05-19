from abc import ABC, abstractmethod

class BaseModel:
    def __init__(self, id: str, name: str, desc: str, supports_sourcecode=False, supports_bytecode=False) -> None:
        self.id = id
        self.name = name
        self.desc = desc
        self.supports_sourcecode = supports_sourcecode
        self.supports_bytecode = supports_bytecode

    @abstractmethod
    def analyze(self, code) -> 'Analysis':
        from lib.analysis.analysis import Analysis
        pass

    def toDict(self):
        return {
            'id': self.id,
            'name': self.name,
            'desc': self.desc,
            'supports_sourcecode': self.supports_sourcecode,
            'supports_bytecode': self.supports_bytecode,
        }
