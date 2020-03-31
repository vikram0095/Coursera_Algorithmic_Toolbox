# Uses python3
def calc_fib(n):
    if n<=1:
    	fib2=n
    else:
    	fib1=0
    	fib2=1
    	for i in range(2,n+1):
    		fib=fib1+fib2
	    	fib1=fib2
	    	fib2=fib
    return fib2
n = int(input())
print(calc_fib(n))
