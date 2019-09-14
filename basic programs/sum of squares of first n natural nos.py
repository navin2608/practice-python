n=int(input("enter a no\n"))
l=list(range(1,n+1))
op=[i**2 for i in l ]
result=sum(op)
print(result)
