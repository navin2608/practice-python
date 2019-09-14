a=list(map(int,input("enter array of elements\n").split()))
max=a[0]
for i in range(1,len(a)):
    if a[i]>max:
        max=a[i]
print("maximum element",max)
