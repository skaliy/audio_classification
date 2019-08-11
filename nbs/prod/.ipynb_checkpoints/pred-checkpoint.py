#!/usr/bin/env python
# coding: utf-8

# In[7]:


from pathlib import Path 
from fastai.vision import *
import os 
import socket

path = os.getcwd()
path = Path(f'{path}/model')

def pred (learner, img_path):
    img = open_image(img_path)
    pred_class,pred_idx,outputs = learner.predict(img)
    return pred_class.obj


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 9980))
s.listen(1)


defaults.device = torch.device('cpu')
learn_melspecs = load_learner(path)

while True:
    conn, addr = s.accept()
    data = conn.recv(1024)
    conn.close()
    pred_class = pred(learn_melspecs, data)
    print(pred_class)





