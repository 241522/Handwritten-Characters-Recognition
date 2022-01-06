import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from .processing import process_image


def predict_character(filename, model, mapping):
    im = Image.open(filename)
    new_im = process_image(im)
    plt.imshow(new_im[0], cmap="gray")
    plt.show()

    prediction = np.argmax(model.predict(new_im))
    print(f" Predicted class={prediction}, which is \"{chr(mapping[prediction])}\" character. ")
