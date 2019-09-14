def monotonic(a):
    return(all(a[i]>=a[i+1] for i in range(len(a)-1)) or all(a[i]<=a[i+1] for i in range(len(a)-1)))
k=list(map(int,input("enter array of elements").split()))
print(monotonic(k))
