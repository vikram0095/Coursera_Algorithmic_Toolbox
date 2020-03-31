# python3

def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 1
    a=numbers[0]
    b=numbers[1]
    if(a<b):
        c=a
        a=b
        b=c
    for first in range(n-2):
        if(numbers[first+2]>=a):
            b=a;
            a=numbers[first+2]
        elif(numbers[first+2]>=b):
            b=numbers[first+2]
    return a*b
#print(max_pairwise_product([1,2,3,1,1,1,3]))

if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
