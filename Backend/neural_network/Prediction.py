import re
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from .processing import process_image


class Prediction(dict):
    LABEL_REGEX_PATTERN = "^LABEL_[a-zA-Z0-9]_$"

    def __init__(self, filename, character):
        dict.__init__(self, filename = filename, character= character, label = None)

        self.load_label()

    def load_label(self):
        possible_label = self["filename"][0:8]
        if re.match(self.LABEL_REGEX_PATTERN, possible_label):
            self["label"] = possible_label[6]


def predict_character(file, model, mapping):
    im = Image.open(file)
    new_im = process_image(im)

    prediction = np.argmax(model.predict(new_im))
    print(f" Predicted class={prediction}, which is \"{chr(mapping[prediction])}\" character. ")
    return Prediction(file.name, chr(mapping[prediction]))
