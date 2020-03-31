# Uses python3
import sys
import numpy as np
def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    vlp=np.divide(values,weights)
    ind=np.argsort(vlp)[::-1]
    ch=0
    while capacity>0 and ch<len(vlp):
        wt=weights[ind[ch]]
        vl=values[ind[ch]]
        temp=capacity-wt
        #print(temp)
        if temp>=0:
            capacity=temp
            value=value+vl
        else:
            value=value+capacity*vlp[ind[ch]]
            capacity=0
        ch=ch+1
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
