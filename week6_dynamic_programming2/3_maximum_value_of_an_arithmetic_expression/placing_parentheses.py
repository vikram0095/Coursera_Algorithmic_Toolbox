import numpy as np
# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def get_maximum_value(vals,op):
    #write your code here
    size_N=len(vals)
    Maxx=np.zeros([size_N,size_N])-1000000000
    Minn=np.zeros([size_N,size_N])+1000000000
    for count in range(len(vals)):
        for s in range(len(vals)-count):
            j=count+s
            i=s
            #print(str(i)+' and '+str(j))
            if i==j:
                Maxx[i,j]=vals[i]
                Minn[i,j]=vals[i]
            else:
                for k in range(i,j):
                   a= evalt(Maxx[i,k], Maxx[k+1,j], op[k])
                   b= evalt(Maxx[i,k], Minn[k+1,j], op[k])
                   c= evalt(Minn[i,k], Maxx[k+1,j], op[k])
                   d= evalt(Minn[i,k], Minn[k+1,j], op[k])
                   Maxx[i,j]=max(Maxx[i,j],a,b,c,d)
                   Minn[i,j]=min(Minn[i,j],a,b,c,d)
                   
    return(int(Maxx[0,size_N-1]))

def get_op_and_num(str):
    vals=[]
    op=[]
    for i in range(len(str)):
        chari=str[i]
        if chari == '+':
            op.append('+')
        elif chari == '-':
            op.append('-')
        elif chari == '*':
            op.append('*')
        else:
            vals.append(int(chari))
    return vals,op

if __name__ == "__main__":
    vals,op=get_op_and_num(input())
    print(get_maximum_value(vals,op))
