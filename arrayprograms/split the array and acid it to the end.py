k=list(map(int,input("enter array of elements").split()))
n=int(input("enter how value is to be splitted"))
l=k[n:]
for i in range(n):
    l.append(k[i])
print(l)

    
    
