a=[8,7,3,5,10,1]
for i in range(len(a)):
    minpos=i
    for j in range(i,len(a)):
        if (a[j]<a[minpos]):
            minpos=j
    a[i],a[minpos]=a[minpos],a[i]
print(a)
            
