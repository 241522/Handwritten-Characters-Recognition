from emnist import extract_training_samples, extract_test_samples
import matplotlib.pyplot as plt
from keras.models import Sequential, load_model, save
from keras.layers import Conv2D, Flatten, Dense, MaxPooling2D, Dropout, BatchNormalization
from keras import callbacks
import keras_tuner as kt
import joblib

def build_model(hp):
    model = Sequential()
    # The first two layers with 32 filters of window size 3x3

    filters = hp.Choice('filters', [64, 128])

    model.add(Conv2D(filters, (3, 3), padding='same', activation='relu', input_shape=(28, 28, 1)))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    for i in range(hp.Int("conv_layers (-1)", 1, 3)):
        model.add(Conv2D(filters, (3, 3), padding='same', activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Flatten())

    dense_layers = hp.Int("dense_layers", 1, 2)
    dropout = hp.Boolean("dropout")
    dense_neurons = hp.Choice('neurons (dense)', [64, 128, 256])

    for i in range(dense_layers):
        model.add(Dense(dense_neurons, activation="relu"))
        if dropout:
            model.add(Dropout(0.25))
    model.add(Dense(62, activation="softmax"))
    model.compile(
        loss="sparse_categorical_crossentropy", metrics=["accuracy"], optimizer="adam",
    )
    return model


def get_model():
    model = Sequential()
    model.add(Conv2D(128, (5, 5), padding='same', activation='relu', input_shape=(28, 28, 1)))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(128, (5, 5), padding='same', activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(128, (5, 5), padding='same', activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Flatten())
    model.add(Dense(64, activation='relu'))
    model.add(Dense(62, activation="softmax"))

    model.compile(
        loss="sparse_categorical_crossentropy", metrics=["accuracy"], optimizer="adam",
    )
    return model

def train_model():
    x_train, y_train = extract_training_samples('byclass')
    x_test, y_test = extract_test_samples('byclass')
    model = get_model()
    history = model.fit(x_train/255, y_train, batch_size=128, epochs=5, validation_data=(x_test/255, y_test))
    plot_history(history)
    save_model(model)
    save_history(history)

def tune(x_train, y_train, x_test, y_test):
    tuner = kt.RandomSearch(
        build_model,
        objective='val_accuracy',
        max_trials=12,
        directory="C:\\Studia\\Semestr_9\\Multimedia\\Handwritten_Characters_Recognition\\logs\\tb")

    tuner.search(x_train,
                 y_train,
                 batch_size=128,
                 epochs=5,
                 validation_data=(x_test, y_test),
                 callbacks=[callbacks.TensorBoard(
                     "C:\\Studia\\Semestr_9\\Multimedia\\Handwritten_Characters_Recognition\\logs\\tb_logs")])

def save_model(model):
    filename_model = 'my_model'
    model.save(filename_model)

def save_history(history):
    filename_history = 'finalized_model_history.history'
    joblib.dump(history, filename_history)

def plot_history(history):
    plt.plot(history.history['accuracy'])
    plt.plot(history.history['val_accuracy'])
    plt.title('model accuracy')
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='upper left')
    plt.show()

    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('model loss')
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='upper left')
    plt.show()