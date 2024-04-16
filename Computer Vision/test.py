import os
import numpy as np
import tensorflow as tf
from PIL import Image
import pandas as pd

model = tf.keras.models.load_model('classification.h5')

class_path = 'labels.csv'
classes = pd.read_csv(class_path)
class_names = list(classes['Name'])

test_dir = 'TEST'
test_images = os.listdir(test_dir)
pred=[]
for i, img_file in enumerate(test_images):
    if(i%10==0):
        print('{} Predicted ',i)
    img_path = os.path.join(test_dir, img_file)
    
    img = Image.open(img_path)
    img = img.resize((256, 256)) 
    imgp = np.array(img) / 255.0 
    
    predictions = model.predict(np.expand_dims(imgp, axis=0), verbose=0)
    predicted_class_index = np.argmax(predictions)
    predicted_class = class_names[predicted_class_index]
    pred.append(predicted_class)

print('done')
print(pred)
    