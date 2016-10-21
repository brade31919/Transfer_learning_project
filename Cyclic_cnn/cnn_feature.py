import numpy as np
import numpy.linalg as la
import math
import itertools
import scipy.ndimage

#all feature extract from the batch
#expected to be a 2D list of np array (num of images in batch)*(Region proposal in one images):5*300
#[map1, map2, map3, map4....]
class fdb(object):
    def __init__(self,features,neighbor,circle):
        self.data = features #data of the 2D list
        self.ft_len = (np.asarray(features)).shape[1] #how many images extracted from one image
        self.im_len = (np.asarray(features)).shape[0] #how many images in one batch
        self.k_nearest = neighbor
        self.circle = circle

    #get the certain feature map
    def get_ft(self,im_num,ft_num):
        assert self.data[im_num][ft_num].size >0
        return self.data[im_num][ft_num]

    #get the shape of certain feature map
    def get_ft_shape(self,im_num,ft_num):
        assert self.data[im_num][ft_num].size >0
        return self.data[im_num][ft_num].shape

    def get_dist(self,im_num1,ft_num1,im_num2,ft_num2):
        #calculate the euclidean distance between 2 map
        #load the two feature map
        a =self.get_ft(im_num1,ft_num1)
        b =self.get_ft(im_num2,ft_num2)
        assert a.shape == b.shape
        dist = la.norm(a-b)

        return dist

    def Cnr(self,n,r):
        output =[list(x) for x in itertools.combinations(n,r)]
        return output

    def pair_unique(self,input):
        unique = []
        for i in input:
            same=0
            for j in unique:
                if i==j:
                    same=1
                    break
            if same==0:
                unique.append(i)

        return unique

    def knn(self):
        #k define k nearest neighbor
        k=self.k_nearest
        M = self.im_len
        L = self.ft_len
        knn_list = [0 for _ in range(M)]

        for im in range(M):
            temp = []
            for ft in range(L):
                dist_info =np.zeros([M,L])
                for i in range(M):
                    for j in range(L):
                        #calculate the distance between feature(im,ft) and feature(i,j)
                        d = self.get_dist(im,ft,i,j)
                        dist_info[i,j]=d
                neighbor=np.argsort(dist_info.flatten())
                im_set = neighbor/L
                ft_set = neighbor%L
                comb = np.column_stack((im_set,ft_set))
                assert comb[0][0] ==im
                temp.append(comb[1:k+1].tolist())
            knn_list[im] = temp

        return knn_list

    def find_circle(self):
        #find the proposal that forms a circle and return that circle
        #N is the N-circle
        N = self.circle
        knn = self.knn()
        M = self.im_len
        L = self.ft_len
        cir = []
        for im in range(M):
            for ft in range(L):
                search = [[] for _ in range(N+1)]
                search[0]=[[im,ft]]
                for j in range(1,N+1):

                    for t in range(len(search[j-1])):
                        search[j]+=knn[search[j-1][t][0]][search[j-1][t][1]][0:self.k_nearest]

                mid = [a for a,b in enumerate(search[N]) if b[0]==im and b[1]==ft]
                if len(mid)==0:
                    continue

                for m in range(len(mid)):
                    bid =[0 for _ in range(N+1)]
                    b = [0 for _ in range(N+1)]
                    bid[N]=mid[m]
                    b[N]=search[N][bid[N]]
                    for i in range(N-1,-1,-1):
                        bid[i] = int(math.ceil(bid[i+1]/(self.k_nearest)))
                        b[i]= search[i][bid[i]]

                    if len(self.pair_unique(b)) < N:
                        continue
                    cir.append(b)


        pos = [0 for _ in range(len(cir))]
        for p in range(len(cir)):
            pos[p]= self.Cnr(cir[p][1:-2],2)

        pos2=[]
        for _ in pos:
            pos2+=_

        ind =[]
        for a,b in enumerate(pos2[0]):
            if b>pos2[1][a]:
               ind.append(a)


        for idx in ind:
            temp=pos2[idx][0]
            pos2[idx][0]=pos2[ind][1]
            pos2[idx][1]=temp

        return self.pair_unique(pos2)

