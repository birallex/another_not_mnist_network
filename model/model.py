from keras import layers
from keras import models
from keras import optimizers

def build_alpha_model():
    model = models.Sequential()
    model.add(layers.Conv2D(128, (3, 3), activation = 'relu', input_shape=(45, 45, 1)))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(256, (3, 3), activation = 'relu'))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(256, (3, 3), activation = 'relu'))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Flatten())
    model.add(layers.Dense(512, activation = 'relu'))
    model.add(layers.Dense(82, activation = 'softmax'))
    print(model.summary())
    return model