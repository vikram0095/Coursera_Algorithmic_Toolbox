# Uses python3
import sys

def get_change(m):
    #write your code here
   
    numcoins=[0]
    coins=[1,3,4]
    for j in range(1,m+1):
        numcoins.append(1000)
        for i in range(len(coins)):
            if(j-coins[i]>0):
                numcoins[j]=min(numcoins[j],1+numcoins[j-coins[i]])
            elif j-coins[i]==0:
#                print(j)
#                print(len(numcoins))
                numcoins[j]=1
    return numcoins[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
#print(get_change(4))