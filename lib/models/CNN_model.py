from lib.vulnerabilites.vulnerability import Vulnerability
from lib.models.base_model import BaseModel
from lib.analysis.analysis import Analysis
import tensorflow as tf
from PIL import Image
import numpy as np
import cv2


class CNNModel(BaseModel):
    def __init__(self) -> None:
        super().__init__(
            id="cnn",
            name="CNN",
            desc="Test",
            supports_bytecode=True,
            supports_sourcecode=False,
        )

    def byte_to_image(self, stg):
        stg = stg.ljust(222**2, "0")
        iterator = 2
        stg = stg[2:]
        image = Image.new(mode="RGB", size=(37, 37))
        y = 0
        x = 0
        while y < 37:
            image.putpixel(
                (x, y),
                (
                    int(stg[iterator : iterator + 2], 16),
                    int(stg[iterator + 2 : iterator + 4], 16),
                    int(stg[iterator + 4 : iterator + 6], 16),
                    255,
                ),
            )
            x += 1
            if x == 36:
                y += 1
                x = 0
            iterator += 6
        return image

    def analyze(self, code) -> Analysis:
        is_bytecode = True

        if not is_bytecode:
            raise Exception("CNNModel only supports bytecode")

        model = tf.keras.Sequential()
        model.add(tf.keras.models.load_model("model_instances/Cnn_model_vf.keras"))
        image = self.byte_to_image(code)

        np_img = np.array(image)

        _, img_buffer = cv2.imencode(".png", np_img)
        img = cv2.imdecode(img_buffer, cv2.IMREAD_COLOR)

        resize = tf.image.resize(img, (37, 37))

        result = model.predict(np.expand_dims(resize / 255, 0))

        labels = [
            "access-control",
            "arithmetic",
            "other",
            "reentrancy",
            "safe",
            "unchecked-calls",
        ]
        vulnerabilites = [
            Vulnerability(
                "1", labels[np.argmax(result[0])], labels[np.argmax(result[0])]
            ),
        ]

        if vulnerabilites[0].name == 'safe': vulnerabilites = []

        return Analysis(
            model_used=self, analyzed_code=code, vulnerabilites=vulnerabilites
        )
