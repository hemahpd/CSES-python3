
for _ in range(int(input())):
    a,b=map(int,input().split())
    tot=a+b
    if (tot % 3 == 0) and (min(a,b)*2>=max(a,b)):
        print("YES")
    else:
        print("NO")
    