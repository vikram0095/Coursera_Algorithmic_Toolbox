# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    sum=fibonacci_sum_naive(to)-fibonacci_sum_naive(from_-1)
    return sum % 10

def pisanoPeriod(m): 
    previous, current = 0, 1
    for i in range(0, m * m): 
        previous, current = current, (previous + current) % m 
          
        # A Pisano Period starts with 01 
        if (previous == 0 and current == 1): 
            return i + 1

def fibonacci_sum_naive(n):
    if n <= 0:
        return 0
    if n <= 1:
        return n

    previous = 0
    current  = 1
    n_new=(n+2)%(pisanoPeriod(10))
    for _ in range(n_new-1):
        previous, current = current , (previous + current)%10

    return (current-1)%10
    


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))
