import numpy as np
import tensorflow as tf
from tensorflow import keras
import lime
from lime import lime_image
from skimage.segmentation import mark_boundaries
from tensorflow.keras.preprocessing import image
import os
import matplotlib.pyplot as plt
from PIL import Image

model = tf.keras.models.load_model(os.path.join('server/static/model.h5'), compile=False)
explainer = lime_image.LimeImageExplainer()
types = ['No_Finding', 'Enlarged_Cardiomediastinum', 'Cardiomegaly', 'Lung_Opacity', 'Lung_Lesion', 'Edema',
         'Consolidation', 'Pneumonia', 'Atelectasis', 'Pneumothorax', 'Pleural_Effusion', 'Pleural_Other',
         'Fracture', 'Support_Devices']


def img_to_tensor(img):
    img = image.load_img(img, target_size=(224, 224), color_mode="rgb")
    img_tensor = image.img_to_array(img)
    img_tensor = np.expand_dims(img_tensor, axis=0)
    img_tensor /= 255.
    temp = img_tensor[0]
    return img_tensor, temp


def explanation_img(img, pathologies, path, view):
    explanation = explainer.explain_instance(img, model.predict, labels=types, hide_color=0,
                                             num_samples=1000, top_labels=len(types))
    for i in explanation.top_labels:
        temp, mask = explanation.get_image_and_mask(i, positive_only=False, num_features=5,
                                                    hide_rest=False)
        plt.title("Pathologie: %s" % (types[i]))
        plt.imshow(img)
        plt.imshow(mark_boundaries(temp, mask))
        full_path = path + types[i] + '_' + view + '.png'
        plt.savefig(full_path)
        full_path = full_path.replace('server/static/img', '')
        pathologies[types[i]].append(full_path)
    return pathologies

def get_prediction(img, action, view):
    pathologies = {}
    tensor, original = img_to_tensor(img)
    res = model.predict(tensor)
    res = np.around(res, decimals=2)
    res = res.astype(float)[0]
    for i in range(len(types)):
        pathologies[types[i]] = [int(round(res[i])), round(res[i], 2)]
    path = str(img).split('\\')
    explanations_path = ""
    for p in path[-6:-1]:
        explanations_path += p + '/'
    if action != "Predict":
        pathologies = explanation_img(original, pathologies, explanations_path, view)
    return pathologies

def predict_all(action, frontal=None, lateral=None):
    pathologies = {}
    if frontal is not None and lateral is not None:
        pathologies_frontal = get_prediction(frontal, action, "frontal")
        pathologies_lateral = get_prediction(lateral, action, "lateral")
        for i in types:
            if pathologies_frontal[i][1] >= pathologies_lateral[i][1]:
                pathologies[i] = pathologies_frontal[i]
            else:
                pathologies[i] = pathologies_lateral[i]
    elif frontal is not None:
        pathologies = get_prediction(frontal, action, "frontal")
    else:
        pathologies = get_prediction(lateral, action, "lateral")
    return pathologies

