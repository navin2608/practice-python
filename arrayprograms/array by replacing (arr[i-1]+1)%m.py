a=list(map(int,input().split()))
b=int(input("enter the divisor"))
l=[]
for x in range(len(a)):
    if a[x]==-1:
        
        a[x]=(a[x-1]+1)%b
        

print("resultant array", a)
