from itertools import combinations
#N,M,K=map(int,input().split())
N,M,K=6,0,3
#A=list(map(int,input().split()))
A=[1,2,4,0,3,4]
D=1
B2=set()
B=combinations(A,K)
for i in B:
    C=tuple(sorted(list(i)))
    B2.add(C)
B2=list(B2)
for i in range(len(B2)):
    for j in B2[i]:
        D*=j
    if D==M:
        C=B2[i]
        break
    D=1
for i in C:
    for j in range(len(A)):
        if i==A[j]:
            A[j]=-1
            print(j+1,end=' ')
            break
