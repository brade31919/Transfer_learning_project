import GoogleSV as gs
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import PanoProcess as pp
import os
import subprocess

save_dir = '/home/Horatio/streetview/'
BaseUri = 'http://maps.google.com/cbk'
#CENTER = '%s,%s' % (25.0454202604, 121.55787478)
a = pp.GetPanoID((24.8241028,121.7719336))
if not(os.path.isdir(save_dir)):
    subprocess.call('mkdir -p %s'%save_dir, shell=True)
url = gs.getpanobyID(a,DIR=save_dir)
print (a)
print (url)



