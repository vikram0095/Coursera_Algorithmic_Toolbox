# Uses python3
import sys

def gcd_naive(a, b):
    if b>=a:
    	if b%a==0:
    		current_gcd=a
    	else:
    		current_gcd=gcd_naive(a,b%a)
    else:
    	current_gcd=gcd_naive(b,a)


    return current_gcd

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_naive(a, b))
