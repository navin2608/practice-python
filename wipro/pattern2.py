n,start=list(map(int,input().split()))

for i in range(n):
    for j in range(i+1):
        print(start,end=" ")
    start+=1
    print()
start-=1
for i in range(n,0,-1):
    for j in range(i):
        print(start,end=" ")
    start-=1
    print()

    
    
 
 
