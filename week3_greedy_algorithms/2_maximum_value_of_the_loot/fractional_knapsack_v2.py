# Uses python3
import sys
import numpy as np
def get_optimal_value(capacity, weights, values):
    value = 0.
    n=len(weights)
    valperwt=np.divide(values,weights)
    print(valperwt)
    ind =((np.argsort(valperwt))[::-1])
    print(ind)
    print(n-1-ind)
    current_choice=0
    while capacity>0:
    	print(capacity-weights[ind[current_choice]])
    	if capacity-weights[ind[current_choice]] >= 0:
    		capcaity=capacity-weights[ind[current_choice]]
    		value=value+weights[ind[current_choice]]
    	else:
    		capcaity=0
    		value=value+(weights[ind[current_choice]]-capacity)*values[ind[current_choice]]/weights[ind[current_choice]]
    	current_choice=current_choice+1
    	#print(capacity)
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
