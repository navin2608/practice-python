l=list(map(int,input("enter array of elements").split()))
n=int(input('enter the no of rotation'))
f=l[2:]
for x in range(n):
    f.append(l[x])
print(f)
