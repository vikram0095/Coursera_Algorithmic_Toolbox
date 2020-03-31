# Uses python3
import sys
import math
def get_number_of_inversions(a):
    aa,inv=merge_sort(a)
    return inv    
    
def merge_sort(a):
    #left, right = 0, len(a)
    if(len(a)==1):
        return a,0
    else:
        inv=0
        mid=math.floor(0.5*(len(a)))
        al,invl=merge_sort(a[:mid])
        ar,invr=merge_sort(a[mid:])
        af=[]
        rr=0
        ll=0
        for i in range(len(al)+len(ar)):
            if(rr==len(ar)):
                af.append(al[ll])
                ll=ll+1 
            elif(ll==len(al)):
                af.append(ar[rr])
                rr=rr+1
            elif(al[ll]<=ar[rr]):
                af.append(al[ll])
                ll=ll+1
            elif(al[ll]>ar[rr] ):
                af.append(ar[rr])
                rr=rr+1 
                inv+=len(al)-ll
            else:
                print('f***ed')

    return af,inv+invl+invr
    
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(get_number_of_inversions(a))
