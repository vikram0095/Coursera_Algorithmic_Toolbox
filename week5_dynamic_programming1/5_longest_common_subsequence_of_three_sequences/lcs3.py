#Uses python3

import sys

import numpy as np

def lcs3(s, t,v):
    d=np.zeros([len(s)+1,len(t)+1,len(v)+1])
    for i in range(len(s)+1):
        for j in range(len(t)+1):
            for k in range(len(v)+1):
                if i==0:
                    d[i,j,k]=0
                elif j==0:
                    d[i,j,k]=0
                elif k==0:
                    d[i,j,k]=0
                else:
                    if s[i-1]==t[j-1] and s[i-1]==v[k-1]:
                        d[i,j,k]=max(d[i-1,j-1,k-1]+1,
                         d[i-1,j-1,k],
                         d[i-1,j,k-1],
                         d[i-1,j,k],
                         d[i,j-1,k-1],
                         d[i,j-1,k],
                         d[i,j,k-1])
                    else:
                        d[i,j,k]=max(d[i-1,j-1,k-1],
                         d[i-1,j-1,k],
                         d[i-1,j,k-1],
                         d[i-1,j,k],
                         d[i,j-1,k-1],
                         d[i,j-1,k],
                         d[i,j,k-1])
    return int(d[len(s),len(t),len(v)])
#
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
#a=[8,3,2,1,7]
#b=[8,2,1,3,8,10,7]
#c=[6,8,3,1,4,7]
#print(lcs3(a, b, c))
