n=int(input())
set1=[]
set2=[]
sum=0
total=n*(n+1)/2
if total%2!=0:
    print("NO")
else:
    print("YES")
    total//=2
    for i in range(n,0,-1):
        if sum+i <=total:
            sum+=i
            set1.append(i)
        else:
            set2.append(i)
    print(len(set1))
    print(*(set1))
    print(len(set2))
    print(*(set2))
