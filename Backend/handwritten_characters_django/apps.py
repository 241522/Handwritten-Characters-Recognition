import pathlib
from django.apps import AppConfig
from neural_network.prediction import predict_character
from keras.models import load_model

class InitialConfig(AppConfig):
    name = 'handwritten_characters_django'
    verbose_name = "Characters Recognition"
    model = None

    def ready(self):
        print("Config working")
        # path = pathlib.Path(__file__).parent.parent.joinpath("neural_network/my_model")
        # print(path)
        # model = load_model(path)
        # print(model.summary())
