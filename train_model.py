import numpy as np
import matplotlib.pyplot as plt

from model.model import build_alpha_model
from keras.preprocessing.image import ImageDataGenerator
from keras import optimizers


def plot_accuracy(history):
    acc = history.history['acc']
    val_acc = history.history['val_acc']
    epochs = range(1, len(acc) + 1)
    plt.plot(epochs, acc, 'bo', label='Training acc')
    plt.plot(epochs, val_acc, 'b', label='Validation acc')
    plt.title("Training and validation accuracy")
    plt.legend()
    #plt.show()
    plt.savefig('learning_statistics/accuracy.png')

    
def plot_loss(history):
    acc = history.history['acc']
    loss = history.history['loss']
    val_loss = history.history['val_loss']
    epochs = range(1, len(acc) + 1)
    plt.plot(epochs, loss, 'bo', label='Training loss')
    plt.plot(epochs, val_loss, 'b', label='Validation loss')
    plt.title('Training and validation loss')
    plt.legend()
    #plt.show()
    plt.savefig('learning_statistics/loss.png')


train_dir = 'dataset/train/'
validation_dir = 'dataset/valid/'
test_dir  = 'dataset/test'

train_datagen = ImageDataGenerator(
    rescale = 1./255, 
    #rotation_range = 15,
    #width_shift_range = 0.1,
    #height_shift_range = 0.1,
    #shear_range = 0.1,
    #zoom_range = 0.1,
    #horizontal_flip = False,
    #fill_mode = 'nearest'
    )

valid_datagen  = ImageDataGenerator(rescale=1./255)
test_datagen  = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size= (45, 45),
    batch_size = 8,
    color_mode='grayscale',
    class_mode = 'categorical'
    )

valid_generator = valid_datagen.flow_from_directory(
    validation_dir,
    target_size = (45, 45),
    batch_size = 8,
    color_mode='grayscale',
    class_mode = 'categorical'
    )

test_generator = test_datagen.flow_from_directory(
    test_dir,
    target_size = (45, 45),
    batch_size = 8,
    color_mode='grayscale',
    class_mode = 'categorical'
    )  

if __name__ == "__main__":
    model = build_alpha_model()
    #model.compile(loss = 'categorical_crossentropy', optimizer= optimizers.RMSprop(lr=1e-4) , metrics=['acc'])
    model.compile(loss = 'categorical_crossentropy', optimizer= 'adam' , metrics=['acc'])

    history = model.fit_generator(train_generator, steps_per_epoch=16,
     epochs = 500, validation_data=valid_generator, validation_steps = 16)
    
    model.save_weights('model/alpha_model.h5')

    plot_accuracy(history)
    plot_loss(history)
    print(model.evaluate_generator(generator= test_generator))