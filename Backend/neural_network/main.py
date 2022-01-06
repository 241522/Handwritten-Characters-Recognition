import matplotlib.pyplot as plt
from keras.models import Sequential, load_model, save
import numpy as np
from PIL import Image

from prediction import predict_character
from processing import read_mapping


def main():
    loaded_model = load_model("my_model")
    mapping = read_mapping()

    loaded_model.summary()

    image_filename = input("Character image path (press 1 to exit) : ")
    while image_filename != "1":
        predict_character(image_filename, loaded_model, mapping)
        image_filename = input("Character image path (press 1 to exit) : ")


if __name__ == '__main__':
    main()
    exit(0)
