n,x=map(int,input().split())
l=list(map(int,input().split()))
s=[]
for i in range(n):
    for j in range(n):
        if i!=j and l[i]+l[j]==x:
            s.append(i+1)
            s.append(j+1)
            break
if len(s)==0:
    print("IMPOSSIBLE")
else:
    for i in range(2):
        print(s[i],end=" ")