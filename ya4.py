import itertools
N=tuple(map(int,input()))
#N=(1,4,5)
K=int(input())
#K=2
fl=0
A=[]
D=set()
if (5 in N) or (sum(N)%3==0):
    for i in range(len(N)-1):
        for j in range(len(N)):
            if j>i:
                A.append((i,j))
    B=itertools.product(A,repeat=K)
    for i in B:
        C=list(N)
        for j in i:
            C[j[0]],C[j[1]]=C[j[1]],C[j[0]]
        C=int(''.join(map(str,C)))
        D.add(C)
    for i in D:
        if i%5==0 or i%6==0:
            fl+=1
    print(fl/len(D))
else:
    print(0)
