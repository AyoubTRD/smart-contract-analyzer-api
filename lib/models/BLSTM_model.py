import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer  # type: ignore
from tensorflow.keras.preprocessing.sequence import pad_sequences  # type: ignore
from lib.analysis.analysis import Analysis
from lib.models.base_model import BaseModel
from lib.vulnerabilites.vulnerability import Vulnerability


class BLSTMModel(BaseModel):
    def __init__(self) -> None:
        super().__init__(
            id="blstm", name="BLSTM", desc="BLSTM description", supports_sourcecode=True
        )

    def Tokenize(self, source_code, max_sequence_length=512):
        tokenizer = Tokenizer()  # Initialize tokenizer
        tokenizer.fit_on_texts([source_code])
        max_sequence_length = 512
        tokenized_data = tokenizer.texts_to_sequences([source_code])
        padded_data = pad_sequences(tokenized_data, maxlen=max_sequence_length)
        return padded_data

    def analyze(self, source_code):
        model = tf.keras.models.load_model("./model_instances/Blstm_model_vf.h5")
        # data preprocessing before giving it to prediction
        data = self.Tokenize(source_code, 512)

        predictions = model.predict(data)
        labels = [
            "access-control",
            "arithmetic",
            "other",
            "reentrancy",
            "safe",
            "unchecked-calls",
            "locked-ether",
            "bad-randomness",
            "double-spending",
        ]
        threshold = 0.5
        binary_predictions = [1 if pred > threshold else 0 for pred in predictions[0]]
        vulnerabilites = []
        for i in range(len(binary_predictions)):
            if binary_predictions[i]:
                vulnerabilites.append(Vulnerability(i, labels[i], labels[i]))

        return Analysis(
            model_used=self, analyzed_code=source_code, vulnerabilites=vulnerabilites
        )
