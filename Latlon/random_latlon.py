import sys
sys.path.append("/home/Horatio/Google_street/")
import PanoProcess as pp
import random
import GoogleSV
import os
import subprocess


#city information
center = {'Taipei': [25.029657,121.504482],
          'Tokyo':[35.642768,139.666413],
          'Buenos Aires':[-34.639356,-58.504147],
          'Roma':[41.874033, 12.423132],
          'Copenhagen':[55.639482, 12.486336],
          'Rio':[-22.937621, -43.247876]}
radius = {'Taipei': [0.040028,0.063356],
          'Tokyo':[0.115703,0.210972],
          'Buenos Aires':[0.057856,0.129948],
          'Roma':[0.077625,  0.14875],
          'Copenhagen':[0.086713,0.154496],
          'Rio':[0.082937, 0.080357]}

55.726195, 12.640832
#generate random latitude, longitude pair
latlon_list = []
N = 10000
i=0

city = 'Copenhagen'
while(i<N):
    latlon = [center[city][0]+random.random()*radius[city][0],center[city][1]+random.random()*radius[city][1]]
    #print round(latlon[0],7)
    #print round(latlon[1],7)
    i=i+1
    latlon_list.append((latlon[0],latlon[1]))
print sys.getsizeof(latlon_list)
print latlon_list

#try getID
ID_list = []
i = 0
while(i<N):
    latlon = latlon_list[i]
    try:
        ID_list.append(GoogleSV.getIDbyloc(lat = latlon[0], lon = latlon[1]))
    except:
        ID_list.append(None)
    i = i+1
print ID_list
print sys.getsizeof(ID_list)

#pick out the valid latlon
valid = []
test = []
iterate = []
i=0
while(i<N):
	if ID_list[i] != None:
		valid.append(latlon_list[i])
		test.append(ID_list[i])
		iterate.append(GoogleSV.getLocationbyID(ID_list[i],1))
	i = i+1
print valid
print iterate
print (iterate[0][0])
print sys.getsizeof(iterate)
#write into file

if os.path.isfile("latlon.txt"):
    subprocess.call("rm latlon.txt",shell = True)

f = open("/home/Horatio/Traveler/latlon.txt",'w')
for element in iterate:
    f.write("(%s,%s)" %(element[0],element[1]))
    f.write("\n")
f.close()

'''
#get pano
save_dir = "./360_pano"
save_dir2 = "./cut"
if not(os.path.isdir(save_dir)):
    subprocess.call('mkdir -p %s'%save_dir, shell=True)
if not(os.path.isdir(save_dir2)):
    subprocess.call('mkdir -p %s'%save_dir2, shell=True)
i= 0
for element in test:
	GoogleSV.getpanobyID(element,DIR=save_dir)
	name = save_dir+"/pano_" + element +".jpg"
	pp.CutPano(name,save_dir2,i)
	i = i+1

while(i<N):
    if ID_list[i] != None:
        GoogleSV.getpanobyID(ID_list[i],DIR=save_dir)
        name = save_dir+"/pano_" + ID_list[i] +".jpg"
        pp.CutPano(name,save_dir2,i)
    i = i+1
'''


