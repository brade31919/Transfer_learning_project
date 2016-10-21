import sys
sys.path.append("/home/Horatio/Google_street/")
import PanoProcess as pp
import os
import glob

N = 10
path = "/home/Horatio/Roma_svdata/"

k = open(path + "record.txt",'r')
count = 0
for line in k:
	count = count+1
print count
'''
i = 0
#file_list = glob.glob(path + "*.txt")
while(i<count):
    a = open(path + "pname"+str(i)+".txt",'r')
    for line in a:
        l = line.split('!')
        for element in l:
            if len(element)==24:
                print(element)
                answer = element[2:]
                print(answer)
    pp.GetPanoByID(answer,"pano_360")
    name = "pano_360/pano_" + answer + ".jpg"
    pp.CutPano(name,"pano",i)
    i = i+1
'''
#########
count = 1600
#########
i = 0
while(i<count):
    j=0
    limit =0
    while(j<8):
        try:
            a = open(path +"old_pname"+str(i)+"-"+str(j)+".txt",'r')
            if(j>0):
                b=open(path +"old_pname"+str(i)+"-"+str(j-1)+".txt",'r')
                for line in a:
                    A = line
                for line in b:
                    B = line
                if A == B:
                    limit = limit-1
            b.close()
            a.close()
            limit = limit+1
        except:
            pass
        j=j+1
    print limit
    j=0    
    while(j<limit):
        print "j = %d"%j
        print limit-1
        try:
            a = open(path +"old_pname"+str(i)+"-"+str(j)+".txt",'r')
            for line in a:
                l = line.split('!')
            for element in l:
                if len(element)==24:
                    answer = element[2:]
                    print(answer)
            pp.GetPanoByID(answer,"old_pano_360",i,j)
            name = "old_pano_360/pano_%05d_%d.jpg"%(i,j)
            pp.CutPano(name,"old_pano",i,j)
        except:
            pass
        j=j+1
        #print "j ="+str(j)
    i = i+1
    #print "i = "+str(i)


