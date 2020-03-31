# Uses python3
import sys

def partition3(A,iter,cap1,cap2,cap3):
    if(iter<len(A)):
        if A[iter]<=cap1 and A[iter]<=cap2 and A[iter]<=cap3:
            return min(partition3(A,iter+1,cap1-A[iter],cap2,cap3),partition3(A,iter+1,cap1,cap2-A[iter],cap3),partition3(A,iter+1,cap1,cap2,cap3-A[iter]))
        elif A[iter]<=cap1 and A[iter]<=cap2:
            return min(partition3(A,iter+1,cap1-A[iter],cap2,cap3),partition3(A,iter+1,cap1,cap2-A[iter],cap3))
        elif A[iter]<=cap2 and A[iter]<=cap3:
            return min(partition3(A,iter+1,cap1,cap2-A[iter],cap3),partition3(A,iter+1,cap1,cap2,cap3-A[iter]))
        elif A[iter]<=cap1 and A[iter]<=cap3:
            return min(partition3(A,iter+1,cap1-A[iter],cap2,cap3),partition3(A,iter+1,cap1,cap2,cap3-A[iter]))
        elif A[iter]<=cap1:
            return partition3(A,iter+1,cap1-A[iter],cap2,cap3)
        elif A[iter]<=cap2:
            return partition3(A,iter+1,cap1,cap2-A[iter],cap3)
        elif A[iter]<=cap3:
            return partition3(A,iter+1,cap1,cap2,cap3-A[iter])
        else:
            return cap1+cap2+cap3
    else:
        return cap1+cap2+cap3


#def partition2(A,iter,cap1,cap2):
#    if(iter<len(A)):
#        if A[iter]<=cap1 and A[iter]<=cap2:
#            return min(partition2(A,iter+1,cap1-A[iter],cap2),partition2(A,iter+1,cap1,cap2-A[iter]))
#        elif A[iter]<=cap1:
#            return partition2(A,iter+1,cap1-A[iter],cap2)
#        elif A[iter]<=cap2:
#            return partition2(A,iter+1,cap1,cap2-A[iter])
#        else:
#            return (cap1-cap2)**2
#    else:
#        return (cap1-cap2)**2



if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
#    A=[3,3,3,3]
    sumA=sum(A)
    if(sumA% 3 !=0):
        print(0)
    else:
        
        cap=int(sumA/3)
#        print(partition3(A,1,cap,cap-A[0],cap))
        if(partition3(A,1,cap,cap-A[0],cap))==0:
            print(1)
        else:
            print(0)