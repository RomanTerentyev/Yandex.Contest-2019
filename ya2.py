N=int(input())
A=[]
for i in range(N):
    A.append(input())
M=int(input())
B=[]
for i in range(M):
    B.append(input())

'''N=4
A=['28-49-5-123-45-67','87544456789','+28 (495) 123 45 56','875-(29)-123456']
M=3
B=['+875 (29) 1XXXXX - Atlantis MythCell',
'+875 (44) 4XXXXX - Atlantis MobTelecom','+28 (495) XXXXXXX - ElDorado GoldLine']'''

Bd=[]
for i in range(len(A)):
    a=''
    for j in A[i]:
        if j.isdigit():
            a+=j
    A[i]=a
for i in range(len(B)):
    a,b='',''
    for j in B[i]:
        if j.isdigit():
            a+=j
        if j=='X':
            b+=j
        if j=='-':
            break
    c=a,b
    Bd.append(c)
for i in A:
    for j in range(len(Bd)):
        if len(i)==(len(Bd[j][0])+len(Bd[j][1])):
            if i.find(Bd[j][0])==0:
                a=i[len(i)-len(Bd[j][1]):len(i)]
                b=''
                k,c=0,0
                while k<len(B[j]):
                    if B[j][k]=='X' and c==0:
                        b+=a
                        k+=len(Bd[j][1])-1
                        c=1
                    else:
                        b+=B[j][k]
                    k+=1
                print(b)
