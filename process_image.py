import os
import cv2
import numpy as np
from model.model import build_alpha_model
from keras.preprocessing import image
import matplotlib.pyplot as plt


classes = []

def get_classes():
    classes = []
    folders_way = 'dataset/test/'
    for folder in os.listdir(folders_way):
        classes.append(folder)
    print("Found class: " + folder)
    classes = sorted(classes)
    return classes


def get_model():
    model = build_alpha_model()
    model.load_weights("model/alpha_model.h5")
    return model


def predict_symbol(img):
    img_arr = np.expand_dims(img, axis=0)
    img_arr = img_arr.reshape((1, 45, 45, 1))
    plt.imshow(img_arr[0], cmap= plt.cm.binary)
    plt.show()
    prediction = model.predict(img_arr).tolist()
    print(prediction)
    prediction = prediction[0]
    index = prediction.index(max(prediction))
    print("Detected symbol: " + classes[index])
    return classes[index]

def letters_extract(image_file: str, out_size=45):
    img = cv2.imread(image_file)
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)
    img_erode = cv2.erode(thresh, np.ones((3, 3), np.uint8), iterations=1)
    contours, hierarchy = cv2.findContours(img_erode, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    output = img.copy()

    letters = []
    for idx, contour in enumerate(contours):
        (x, y, w, h) = cv2.boundingRect(contour)
        # print("R", idx, x, y, w, h, cv2.contourArea(contour), hierarchy[0][idx])
        # hierarchy[i][0]: the index of the next contour of the same level
        # hierarchy[i][1]: the index of the previous contour of the same level
        # hierarchy[i][2]: the index of the first child
        # hierarchy[i][3]: the index of the parent
        if hierarchy[0][idx][3] == 0:
            cv2.rectangle(output, (x, y), (x + w, y + h), (70, 0, 0), 1)
            letter_crop = gray[y:y + h, x:x + w]
            size_max = max(w, h)
            letter_square = 255 * np.ones(shape=[size_max, size_max], dtype=np.uint8)
            if w > h:
                y_pos = size_max//2 - h//2
                letter_square[y_pos:y_pos + h, 0:w] = letter_crop
            elif w < h:
                x_pos = size_max//2 - w//2
                letter_square[0:h, x_pos:x_pos + w] = letter_crop
            else:
                letter_square = letter_crop
            letters.append((x, w, cv2.resize(letter_square, (out_size, out_size), interpolation=cv2.INTER_AREA)))
    letters.sort(key=lambda x: x[0], reverse=False)
    return letters



def img_to_str(image_file: str):
    letters = letters_extract(image_file)
    print(len(letters))
    s_out = ""
    for i in range(len(letters)):
        dn = letters[i+1][0] - letters[i][0] - letters[i][1] if i < len(letters) - 1 else 0
        s_out += predict_symbol(letters[i][2])
        if (dn > letters[i][1]/4):
            s_out += ' '
    return s_out

if __name__ == "__main__":
    classes = get_classes()
    print(classes)
    model = get_model()
    s_out = img_to_str("test_examples/test_formula.png")
    print(s_out) 