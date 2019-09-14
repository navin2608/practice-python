a=[6,8,3,10,2]
for j in range(len(a)-1):
    
    for i in range(len(a)-1):
        if (a[i]>a[i+1]):
            a[i],a[i+1]=a[i+1],a[i]
print(a)
