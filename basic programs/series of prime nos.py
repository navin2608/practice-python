m,n=list(map(int,input().split()))
for i in range(m,n+1):
    if i>2:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i,end=' ')
