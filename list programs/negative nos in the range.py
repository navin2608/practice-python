start=int(input())
end=int(input())
l=list(range(start,end+1))
res=[i*1 for i in l if i<0]
print(res)
