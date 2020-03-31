# Uses python3
import sys
from collections import namedtuple
import random
Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points=[]
    while len(segments)>0:
        mr=segments[min_right(segments)].end
        points.append(mr)
        delete_visited(segments,mr)
#        print(segments)
    return points

def min_right(segments):
    min_index=0
    min_val=segments[0].end
    for i in range(1,len(segments)):
        if segments[i].end<min_val:
            min_val=segments[i].end
            min_index=i
        
    return min_index    

def delete_visited(segments,point_index):
    de=0
    for i in range(len(segments)):
        s=segments[i-de]
        if s.start <= point_index and s.end >= point_index:
            del(segments[i-de])
            de+=1
    
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
