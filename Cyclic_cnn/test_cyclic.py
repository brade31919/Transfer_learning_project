from cnn_feature import fdb
import pickle
import math

with open('./pano_00000_0_0.pkl','rb') as f:
    c = pickle.load(f)

k=fdb(c,4,4)
a=k.knn()
N = k.circle
knn = k.knn()
M = k.im_len
L = k.ft_len
cir = []
im=3
ft=0
search = [[] for _ in range(N+1)]
search[0]=[[im,ft]]
for j in range(1,N+1):

    for t in range(len(search[j-1])):
        search[j]+=knn[search[j-1][t][0]][search[j-1][t][1]][0:k.k_nearest]

mid = [a for a,b in enumerate(search[N]) if b[0]==im and b[1]==ft]
if len(mid)==0:
    pass

print "progress"

for m in range(len(mid)):
    bid =[0 for _ in range(N+1)]
    b = [0 for _ in range(N+1)]
    bid[N]=mid[m]
    b[N]=search[N][bid[N]]
    for i in range(N-1,-1,-1):
        bid[i] = int(math.ceil(bid[i+1]/(k.k_nearest)))
        b[i]= search[i][bid[i]]

    if len(k.pair_unique(b)) < N:
        continue
    cir.append(b)
print cir