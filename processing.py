from tensorflow.keras.models import load_model
import numpy as np
from tensorflow.keras.preprocessing.image import img_to_array

def call_model():
    print("**********LOADING MODEL***************")
    model = load_model("Models/final_model.h5")
    return model

def data_prep(image):
    print("********PROCESSING IMAGE*************")
    if image.mode != 'RGB':
        image = image.convert("RGB")
    image = image.resize((224,224))
    image = np.expand_dims(image,axis=0)
    #image = img_to_array(image)

    return image    