#Uses python3

import sys
import numpy as np
def lcs2(s, t):
    sub_leng=0
    d=np.zeros([len(s)+1,len(t)+1])
    for i in range(len(s)+1):
        for j in range(len(t)+1):
            if i==0:
                d[i,j]=0
            elif j==0:
                d[i,j]=0
            else:
                if s[i-1]==t[j-1]:
                    d[i,j]=max(d[i-1,j-1]+1,d[i-1,j],d[i,j-1])
                else:
                    d[i,j]=max(d[i-1,j-1],d[i-1,j],d[i,j-1])
#    value=d[len(s),len(t)]
#    i=len(s)
#    j=len(t)
#    
#    while(value>0):
#
#        if s[i-1]==t[j-1]:
#            print(s[i-1])
#            if(d[i-1,j-1]+1>= d[i-1,j] and d[i-1,j-1]+1>=d[i,j-1]):
#                value=d[i-1,j-1]
#                sub_leng+=1
#                i=i-1
#                j=j-1
#            elif d[i-1,j] >= d[i,j-1]:
#                value=d[i-1,j]
#                sub_leng+=1
#                i=i-1
#                j=j         
#            else:
#                value=d[i,j-1]
#                sub_leng+=1
#                i=i
#                j=j-1
#        else:
#            if(d[i-1,j-1] >= d[i-1,j] and d[i-1,j-1]>=d[i,j-1]):
#                value=d[i-1,j-1]
#                i=i-1
#                j=j-1
#            elif d[i-1,j] <= d[i,j-1]:
#                value=d[i,j-1]
#                i=i
#                j=j-1        
#            else:
#                value=d[i-1,j]
#                i=i-1
#                j=j
       # print(str(i)+'-'+str(j))

    print(d)
    return int(d[len(s),len(t)])
#
#if __name__ == '__main__':
#    input = sys.stdin.read()
#    data = list(map(int, input.split()))
#
#    n = data[0]
#    data = data[1:]
#    a = data[:n]
#
#    data = data[n:]
#    m = data[0]
#    data = data[1:]
#    b = data[:m]
#
#    print(lcs2(a, b))
print(lcs2([10,4,2,5,55,555,7,4,1],[2,7,0,0,0,0,1]))
