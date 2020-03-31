# Uses python3
import numpy as np

def edit_distance(s, t):
    #write your code here
    d=np.zeros([len(s)+1,len(t)+1])
    for i in range(len(s)+1):
        for j in range(len(t)+1):
            if i==0:
                d[i,j]=j
            elif j==0:
                d[i,j]=i
            else:
                if s[i-1]==t[j-1]:
                    d[i,j]=min(d[i-1,j-1],1+d[i-1,j],1+d[i,j-1])
                else:
                    d[i,j]=min(1+d[i-1,j-1],1+d[i-1,j],1+d[i,j-1])
    #print(d)
    return int(d[len(s),len(t)])

if __name__ == "__main__":
    print(edit_distance(input(), input()))
#print(edit_distance("short","ports"))
