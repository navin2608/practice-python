arr=list(map(int,input().split(',')))

n=int(input("Enter n value"))
l=[]
mul=1
x=0
for i in range(len(arr)):
    x=arr[i]%n
    l.append(x)
for j in range(len(l)):
    mul*=l[j]
print(mul%n)
