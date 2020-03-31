# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    n_new=(n)%(pisanoPeriod(m))
    if n_new <= 1:
        return n_new

    previous = 0
    current  = 1
    for _ in range(n_new- 1):
        previous, current = current, previous + current

    return current % m
def pisanoPeriod(m): 
    previous, current = 0, 1
    for i in range(0, m * m): 
        previous, current = current, (previous + current) % m 
          
        # A Pisano Period starts with 01 
        if (previous == 0 and current == 1): 
            return i + 1



if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
#print(get_fibonacci_huge_naive(9999999999999  , 2))
