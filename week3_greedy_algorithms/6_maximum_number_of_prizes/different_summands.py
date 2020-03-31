# Uses python3
import sys
import math
def optimal_summands(n):
    N=math.floor((math.sqrt(1+8*n)-1)/2)
    del_sum_N=int(n-N*(N+1)*0.5)
    seq=list(range(1,N+1))
    seq[N-1]=seq[N-1]+del_sum_N
    #write your code here
    return seq

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
#optimal_summands(2)