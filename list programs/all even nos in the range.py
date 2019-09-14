start=int(input("starting no"))
end=int(input("ending no"))
l1=[i*1 for i in range(start,end+1) if i%2==0]
print(l1)
