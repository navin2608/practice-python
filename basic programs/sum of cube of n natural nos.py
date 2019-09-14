n=int(input("enter a value\n"))
l=list(range(1,n+1))
op=[i**3 for i in l]
result=sum(op)
print(result)
