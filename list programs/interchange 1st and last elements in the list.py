a=list(map(int,input().split()))
l=len(a)-1
a[0],a[l]=a[l],a[0]
print(a)
