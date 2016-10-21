import numpy as np
from cnn_feature import fdb
import pickle

with open('./pano_00000_0_0.pkl','rb') as f:
    c = pickle.load(f)

k=fdb(c,3,5)
a=k.find_circle()
print a