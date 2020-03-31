# Uses python3
import sys
import numpy as np
import math

def binary_search_index_right(a,left,right,x):
    #left, right = 0, len(a)
    if x<a[left]:
        return left-0.5
    elif x>=a[right]:
        return right+0.5
    
    if right<=left:
        print("haaaaaa")
        return right
    else:
        
        mid=left+math.floor(0.5*(right-left))  
        midr=mid
        midl=mid
        
        while(midr<=right-1):
            if a[midr+1]==a[midr]:
                midr=midr+1
            else:
                break
            
        while(midl>=left+1):
            if a[midl-1]==a[midl]:
                midl=midl-1
            else:
                break
        
        
        if x==a[mid]:
            return midr+0.5
        elif x>a[mid]:
            return binary_search_index_right(a,midr+1,right, x)
        else:
            return binary_search_index_right(a,left,midl, x)
        
        
def binary_search_index_left(a,left,right,x):
    #left, right = 0, len(a)
    if x<=a[left]:
        return left-0.5
    elif x>a[right]:
        return right+0.5
    
    if right<=left:
        print("haaaaaa")
        return right
    else:
        
        mid=left+math.floor(0.5*(right-left))  
        midr=mid
        midl=mid
        
        while(midr<=right-1):
            if a[midr+1]==a[midr]:
                midr=midr+1
            else:
                break
            
        while(midl>=left+1):
            if a[midl-1]==a[midl]:
                midl=midl-1
            else:
                break
        
        
        if x==a[mid]:
            return midl-0.5
        elif x>a[mid]:
            return binary_search_index_left(a,midr+1,right, x)
        else:
            return binary_search_index_left(a,left,midl, x)


def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

#if __name__ == '__main__':
#    input = sys.stdin.read()
#    data = list(map(int, input.split()))
#    n = data[0]
#    m = data[1]
#    starts = data[2:2 * n + 2:2]
#    ends   = data[3:2 * n + 2:2]
#    points = data[2 * n + 2:]
#    #use fast_count_segments
#    cnt = fast_count_segments(starts, ends, points)
#    for x in cnt:
#        print(x, end=' ')
#print(fast_count_segments([0,7],[5,10],[1,6,11]))
#print(fast_count_segments([-10,2,-10,-5,3,3,5],[4,4,6,6,4,5,6],[4,3,2,5,6]))
    
def fast_count_segments(starts, ends, points):
    segs=[]
    for i in range(len(starts)):
        segs.append([ends[i],starts[i]])
    segs.sort()   
#    while True:
    level=0        
    add_const=1
    ind=np.argsort(points)
    points.sort()
    points_count=np.zeros(len(points),dtype=int)
    swtch=0

    while True:

        if level==len(starts)-1:
            start_=segs[level][1]
            end_=segs[level][0]
            print("start_end",start_,end_)
            
            stind=int(0.5+binary_search_index_left(points,0,len(points)-1,start_))
            endind=int(-0.5+binary_search_index_right(points,0,len(points)-1,end_))
            print("index in points",stind,endind)
            
            print("Add",add_const)
            
            for jjj in range(stind+swtch,endind+1):
                points_count[jjj]+=add_const
            break
        
        
        elif segs[level+1][0]==segs[level][0]:
            start_=segs[level][1]
            end_=segs[level+1][1]
            print("start_end",start_,end_)

            stind=int(0.5+binary_search_index_left(points,0,len(points)-1,start_))
            endind=int(-0.5+binary_search_index_right(points,0,len(points)-1,end_))
            print("index in points",stind,endind)
            
            print("Add",add_const)

            for jjj in range(stind+swtch,endind+1):
                points_count[jjj]+=add_const
            swtch=0
            
            if points[endind]==end_:
                print("Overlap",end_)
                points_count[endind]+=1
                swtch=1
        else:
            start_=segs[level][1]
            end_=segs[level][0]
            stind=int(0.5+binary_search_index_left(points,0,len(points)-1,start_))
            endind=int(-0.5+binary_search_index_right(points,0,len(points)-1,end_))
            print("index in points",stind,endind)
            print("start_end",start_,end_)
            print("Switch",swtch)
            for jjj in range(stind+swtch,endind+1):
                points_count[jjj]+=add_const
                swtch=0
            add_const=0
            
        print(points_count,'\n',points,'\n')

        level+=1
        add_const+=1
        

    print(points_count,'\n',points,'\n')
    print(ind)
    litt=np.zeros(len(points),dtype=int)
    for zz in range(len(points)):
        litt[ind[zz]]=(int(points_count[zz]))
    print('\n\n')
    return litt
#print(fast_count_segments([0,7],[5,10],[1,6,11]))

#print(fast_count_segments([-10,2,-10,-5,3,3,5,2],[4,4,6,6,4,5,6,4],[2,3,4,5,6]))
#print(fast_count_segments([0,-3,7],[5,2,10],[1,6]))
print(fast_count_segments([0,2],[2,4],[0,1,4,4,4,4,2]))
#
#0 2
#2 4
#0 1 3 4 4 4 4 4 2
##a=[0,1,2,2,2,2,3,4,4]
##x=2.5
##print(binary_search_index_left(a,0,len(a)-1,x))
##print(binary_search_index_right(a,0,len(a)-1,x))