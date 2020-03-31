#Uses python3

import sys
import random
def max_dot_product(a, b):
    #write your code here
    res = 0
    randomized_quick_sort(a,0,len(a)-1)
    randomized_quick_sort(b,0,len(b)-1)
    for i in range(len(a)):
        res += a[i] * b[i]
    return res
def partition3(a, l, r):
    #write your code here
    x = a[l]
    m1 = l
    m2=l
    for i in range(l + 1, r + 1):
        if a[i] < x:
            m1 += 1
            m2+=1
            if m2!=i:
                temp=a[m2]
                a[m2]= a[m1]
                a[m1]= a[i]
                a[i] = temp
            else:
                temp=a[m1]
                a[m1]= a[i]
                a[i] = temp
        elif a[i]==x:
            m2+=1
            a[m2],a[i]=a[i],a[m2]
        else:
            pass    
    a[l], a[m1] = a[m1], a[l]
    return m1-1,m2


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
  
    m1,m2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m1);
    randomized_quick_sort(a, m2+1, r);
    
    
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
#print(max_dot_product([1,2,3],[3,2,1]))

