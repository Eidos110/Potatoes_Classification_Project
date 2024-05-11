import numpy as np
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image



class PredictionPipeline:
    def __init__(self,filename):
        self.filename = filename

    

    def predict(self):
        model = load_model(os.path.join("artifacts","training","model.keras"))

        image_name = self.filename
        test_image = image.load_img(image_name,target_size= (224,224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        prediction = model.predict(test_image)

        if np.argmax(prediction) == 0:
            return [{"image" : 'Potato_Early_blight'}]
        elif np.argmax(prediction) == 1:
            return [{"image" : 'Potato_healthy'}]
        else:
            return [{"image" : 'Potato_Late_blight'}]
             