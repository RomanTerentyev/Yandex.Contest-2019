def formatInput(sequence):
    count=''
    result=[]
    for item in sequence:
        if item.isdigit():
            count+=item
        else:
            if count:
                result.append((item,int(count)))
            else:
                result.append((item,1))
            count=''
    return result


#rle="a2b3ca"
rle=input()
decoded=tuple(formatInput(rle))
q=int(input())
#q=1
for i in range(q):
    l,r = map(int,input().split())
    #l,r=1,1
    nw=[]
    sum=0
    for j in decoded:
        sum+=j[1]
        if l<=sum:
            if (sum-j[1])<l<=r<=sum:
                k=list(j)
                k[1]=r-l+1
                nw.append(tuple(k))
                break
            if r<=sum:
                k=list(j)
                k[1]=k[1]-sum+r
                nw.append(tuple(k))
                break
            if l<sum<r:
                if nw==[]:
                    k=list(j)
                    k[1]=sum-l+1
                    nw.append(tuple(k))
                else:
                    nw.append(j)
            else:
                k=list(j)
                k[1]=l-sum+1
                nw.append(tuple(k))
    #print(nw)
    sum=0
    for j in nw:
        if j[1]==1:
            sum+=1
        else:
            sum=sum+1+len(str(j[1]))
    print(sum)
