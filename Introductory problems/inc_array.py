n=int(input())
b=list(map(int,input().split()))
count=0
for i in range(n-1):
    if b[i] > b[i + 1]:
        count += b[i] - b[i + 1]
        b[i + 1] = b[i]
print(count)