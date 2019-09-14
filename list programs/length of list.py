import timeit
a=list(map(int,input("enter array of elements").split()))
print("length",len(a))
print("time consumed",timeit.timeit())
