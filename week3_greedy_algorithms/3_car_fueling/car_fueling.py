# python3
import sys
import numpy as np

def compute_min_refills(distance, tank, stops):
    # write your code here
    stop=0
    refill=0
    stops.insert(0,0)
    stops.insert(len(stops),distance)
    if np.max(np.subtract(stops[1:],stops[0:-1]))<=tank:
        while distance>0:
            fuel=tank
            #delt=stops[stop+1]-stops[stop]
            #print(delt)
            while fuel>0 and distance > 0 and fuel >= (stops[stop+1]-stops[stop]) :
                #print(stop)
                fuel=fuel-stops[stop+1]+stops[stop]
                distance=distance-stops[stop+1]+stops[stop]
                stop=stop+1
                #print(distance)
            
            refill=refill+1
    return refill-1

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
