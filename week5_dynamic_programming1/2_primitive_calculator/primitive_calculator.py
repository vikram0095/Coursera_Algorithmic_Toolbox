# Uses python3
import sys

def optimal_sequence(n):

    numcoins=[-1]
    seq=[n]
    for j in range(1,n+1):
        numcoins.append(0)
        if j % 6 == 0:
            numcoins[j]=1+min(numcoins[j//3],numcoins[j//2],numcoins[j-1])
        elif j%3==0:
            numcoins[j]=1+min(numcoins[j//3],numcoins[j-1])   
        elif j%2==0:
            numcoins[j]=1+min(numcoins[j//2],numcoins[j-1])
        else:
            numcoins[j]=1+numcoins[j-1]
            j=n
    while j>1:
        if j % 6 == 0:
            if(numcoins[j//3]<=numcoins[j//2] and numcoins[j//3] <=numcoins[j-1]):
                seq.append(j//3)
                j=j//3
            elif numcoins[j//2]<=numcoins[j-1]:
                seq.append(j//2)
                j=j//2
            else:
                seq.append(j-1)
                j=j-1
        elif j%3==0:
            if numcoins[j//3]<=numcoins[j-1]:
                seq.append(j//3)
                j=j//3
            else:
                seq.append(j-1)
                j=j-1
        elif j%2==0:
            if numcoins[j//2]<=numcoins[j-1]:
                seq.append(j//2)
                j=j//2
            else:
                seq.append(j-1)
                j=j-1
        else:
            seq.append(j-1)
            j=j-1
        
          
    return reversed(seq)

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
