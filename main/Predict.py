# -*- coding: utf-8 -*-

from google.colab import drive
drive.mount('/content/gdrive')

import json
import urllib
import os
import sys
sys.path.append('/content/gdrive//MyDrive/VoiceRecognition/main/')
import newlearn

import unicodedata
import numpy as np
import tensorflow as tf
import keras
import torch
from keras import layers, models ,Model ,Input
from keras.layers import Dense, Flatten, Activation, BatchNormalization
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split, KFold
from tensorflow.keras.utils import to_categorical
from keras.callbacks import EarlyStopping


def result_recognition(user_info):
  record_target=[]

  for i, (root, dirs, files) in enumerate (os.walk("/content/gdrive//MyDrive/VoiceRecognition/static/Recording/")):
      for file in files :
          if '.wav'  not in file in file :
              continue
          else :
              audio_path = os.path.join(root,file)
              dirname = os.path.dirname(audio_path) 
              record_target.append(dirname)

  re_encoder = LabelEncoder()
  re_encoder.fit(record_target)
  retarget_encoded = re_encoder.transform(record_target)
  print(record_target, '==>', retarget_encoded)    
      
  path="/content/gdrive//MyDrive/VoiceRecognition/static/Result_recording/"
  
  model = models.load_model("/content/gdrive//MyDrive/VoiceRecognition/main/demo_model.h5")

  test_data=newlearn.make_predx(path,model.input)

  with open("/content/gdrive//MyDrive/VoiceRecognition/static/UserInfo/user_info.json", 'r') as f:
      json_data = json.load(f)
  
#   dec_y=[]

  y_predict = model.predict(test_data)
  y_predict = np.argmax(y_predict)
#   dec_y.append(y_predict)
#   dec_y=np.array(dec_y)
#   print(dec_y)
#   print(re_encoder.inverse_transform(dec_y))

#   dirname=re_encoder.inverse_transform(dec_y)
#   label_y=dirname[0].split("/")
  label_y=json_data[str(y_predict)]

  user_info=unicodedata.normalize('NFC',user_info)
  predict_userinfo=unicodedata.normalize('NFC',label_y)
  
  print("예측한 값 "+predict_userinfo)
  print("실제 값 "+user_info)
  print("예측한 값 길이"+str(len(predict_userinfo)))
  print("실제 값 길이"+str(len(user_info)))
  
  if user_info==predict_userinfo:
    print("success")
    return "success"
  else:
    print("failed")
    return "falied"