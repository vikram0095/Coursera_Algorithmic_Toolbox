# Uses python3
import sys

def get_majority_element(a, left, right):
    mergeSort(a)
    maxn=1
    maxxn=1
    prev=a[0]
    for i in range(1,len(a)):
        curr=a[i]
        if(curr==prev):
            maxn=maxn+1
        else:
            if(maxxn<maxn):
                maxxn=maxn
            maxn=1
        prev=curr
    if(maxxn<maxn):
            maxxn=maxn
        
    if(maxxn>len(a)/2):
        return 1
    else:
        return -1

def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 #Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
  
        mergeSort(L) # Sorting the first half 
        mergeSort(R) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
          
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
