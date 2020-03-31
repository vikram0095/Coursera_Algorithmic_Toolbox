# Uses python3
import sys
import math
def get_change(m):
    #write your code here
    tens=math.floor(m/10);
    fives=math.floor((m-tens*10)/5);
    ones=m-tens*10-fives*5
    return ones+fives+tens

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
