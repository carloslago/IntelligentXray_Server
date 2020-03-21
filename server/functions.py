import numpy as np
import tensorflow as tf
from tensorflow import keras
import lime
from lime import lime_image
from skimage.segmentation import mark_boundaries
from tensorflow.keras.preprocessing import image
import os



model = tf.keras.models.load_model(os.path.join('server/static/model.h5'), compile=False)

def img_to_tensor(img):
    # img_tensor = image.img_to_array(img)
    # img_tensor = np.array(img)
    img = image.load_img(img, target_size=(224, 224), color_mode="rgb")
    img_tensor = image.img_to_array(img)
    img_tensor = np.expand_dims(img_tensor, axis=0)
    img_tensor /= 255.
    return img_tensor


def predict_img(img):
    tensor = img_to_tensor(img)
    res = model.predict(tensor)
    res = np.around(res)
    res = res.astype(int)[0]
    types = ['No_Finding', 'Enlarged_Cardiomediastinum', 'Cardiomegaly', 'Lung_Opacity', 'Lung_Lesion', 'Edema',
             'Consolidation', 'Pneumonia', 'Atelectasis', 'Pneumothorax', 'Pleural_Effusion', 'Pleural_Other',
             'Fracture', 'Support_Devices']
    pathologies = {}
    for i in range(len(types)):
        pathologies[types[i]] = res[i]
    return pathologies