import pathlib

import numpy
from django.apps import AppConfig
from keras.models import load_model
from neural_network.processing import read_mapping


model = None
mapping = None

class InitialConfig(AppConfig):
    name = 'handwritten_characters_django'
    verbose_name = "Characters Recognition"

    def ready(self):
        global model
        global mapping
        print("Config working")
        if model is None:
            model_path = pathlib.Path(__file__).parent.parent.joinpath("neural_network/my_model")
            model = load_model(model_path)
        model.predict(numpy.zeros((1,28,28,1)))
        mapping = read_mapping(pathlib.Path(__file__).parent.parent.joinpath("neural_network/emnist-byclass-mapping.txt"))
        # print(model.summary())
