#Uses python3

import sys
import random
def is_grt_ab(a,b):
    p=a*10**(len(str(b)))+b
    q=b*10**(len(str(a)))+a
    if p>q:
        return True
    else:
        False




def partition3_digit(a, l, r):
    #write your code here
    x = a[l]
    m1 = l
    m2=l
    for i in range(l + 1, r + 1):
        if is_grt_ab(a[i] ,x):
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


def randomized_quick_sort_digit(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
  
    m1,m2 = partition3_digit(a, l, r)
    randomized_quick_sort_digit(a, l, m1);
    randomized_quick_sort_digit(a, m2+1, r);
    
def largest_number(a):
    #write your code here
    randomized_quick_sort_digit(a,0,len(a)-1)
    res = ""
    for x in a:
        res += str(x)
    return res
#
if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
#print(largest_number([1,9,2]))
#print(is_grt_ab(21,2))
