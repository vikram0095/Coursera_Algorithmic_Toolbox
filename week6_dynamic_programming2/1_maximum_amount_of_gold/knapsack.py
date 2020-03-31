# Uses python3
import sys
import numpy as np

def optimal_weight(W, w):
    # write your code here
    d=np.zeros([len(w)+1,W+1])
    for i in range(len(w)+1):
        for j in range(W+1):
            if i==0:
                d[i,j]=0
            elif j==0:
                d[i,j]=0
            else:
                if(w[i-1]<=j):
                    d[i,j]=max(d[i-1,j-w[i-1]]+w[i-1],d[i-1,j])
               
                else:
                    d[i,j]=d[i-1,j]

    #print(d)
    return int(d[len(w),W])


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))

#print(optimal_weight(10,[3,5,3,3,5]))
