#!/usr/bin/env python
# coding: utf-8

# In[1]:


import socket
from pathlib import Path 
import librosa 
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import sys 


# In[ ]:

print(sys.argv[1])
print(sys.argv[2])

def save_specs(audio_fname_path, image_fname_path):
    '''
    create image from wav file
    '''
    y, sr = librosa.load(audio_fname_path, sr=None)
    S = librosa.feature.melspectrogram(y, sr=sr, n_mels=128)
    log_S = librosa.power_to_db(S, ref=np.max)
    librosa.display.specshow(log_S, sr=sr, x_axis='time', y_axis='mel')
    fig1 = plt.gcf()
    plt.axis('off')
    plt.draw()
    fig1.savefig(image_fname_path, bbox_inches='tight', pad_inches=0 ,dpi=100)

example_audio_path = '/home/sathiesh/Desktop/blink_20.wav'
example_img_path = '/home/sathiesh/Desktop/img.png'

#arg 1: wav file path   
#arg 2: audio to image path
save_specs(sys.argv[1], sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 9980))
s.sendall(str.encode(example_img_path))
s.close()