import keras
import numpy as np
import tensorflow as tf
from keras.preprocessing.image import * 
# from keras.utils import to_categorical
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt 
import pandas as pd 
import random
import os 
import time




path = ""


while True:
    filenames2 = os.listdir("./home")
    if len(filenames2)!=0:
        break
    else:
        time.sleep(10)

model = tf.keras.models.load_model('./home/model.h5')
filenames = os.listdir(path+"/data/test")

test_df=pd.DataFrame( {"filename":filenames} )      
test_df

nbsamples=test_df.shape[0]
IMAGE_WIDTH=128
IMAGE_HEIGHT=128
IMAGE_SIZE=(IMAGE_WIDTH, IMAGE_HEIGHT)
batch_size = 16
test_datagen=ImageDataGenerator(rescale=1./255)
# 테스트 이미지니까, 사진 그대로 씀
test_generator=test_datagen.flow_from_dataframe(
    test_df,
    path+"/data/test",
    x_col= "filename",
    y_col= None,
    target_size = IMAGE_SIZE,
    class_mode = None,
    batch_size = batch_size,
    shuffle = False)

predict=model.predict(test_generator)
                       
                                
test_df['category']=np.argmax(predict, axis=1)

test_df['category']=test_df['category'].replace({0:'cat',1:"dog"})
ex_df=test_df.sample(n=50).reset_index(drop=True)
print(ex_df)

ex_generator = test_datagen.flow_from_dataframe(
                    ex_df,
                    path+"/data/test",
                    x_col = "filename",
                    y_col = None,
                    target_size = IMAGE_SIZE,
                    class_mode = None)


test_sample=list(ex_df.filename)

sample = ""
for test in test_sample:
    sample += test