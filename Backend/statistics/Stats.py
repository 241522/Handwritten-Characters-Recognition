import json
import time

from neural_network.Prediction import predict_character, Prediction
from handwritten_characters_django.apps import model, mapping
from feature_based.feature_based_approach import detectCharacter

def calculate_stats(files):
    return get_method_stats(files , "nn"), get_method_stats(files, "fb")

def get_method_stats(files, method):

    predictions = []
    accurate = 0
    labeled = 0
    total_count = len(files)
    time_elapsed = 0


    for f in files:
        start = time.perf_counter()
        if method == "nn":
            prediction = predict_character(f, model, mapping)
        elif method == "fb":
            prediction = Prediction(f.name, detectCharacter(f))
        else:
            raise Exception()
        time_elapsed += time.perf_counter() - start
        if prediction['label'] is not None:
            labeled +=1
        if prediction['label'] == prediction['character']:
            accurate +=1

        predictions.append(prediction)

    return Stats(accurate/total_count, time_elapsed, labeled_count=labeled, total_count=total_count, average_time=time_elapsed/total_count, predictions= predictions)



class Stats:
    def __init__(self, accuracy, time_sum, labeled_count, total_count, average_time, predictions):
        self.accuracy = accuracy
        self.labeled_count = labeled_count
        self.time = time_sum
        self.average_time = average_time
        self.total_count = total_count
        self.predictions = predictions

