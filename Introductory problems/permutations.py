n=int(input())
if n==1:
    print(1)
elif n<=3:
    print("NO SOLUTION")
elif n==4:
    print("2 4 1 3")
else:
    odd=list(range(1,n+1,2))
    even=list(range(2,n+1,2))
    print(*(odd+even))
