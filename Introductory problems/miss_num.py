n=int(input())
l=list(map(int,input().split()))
tot=(n*(n+1))/2
print(int(tot-sum(l)))
