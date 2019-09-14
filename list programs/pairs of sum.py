l=list(map(int,input().split()))
sum=int(input())
a=[]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]+l[j]==sum:
            print(l[i],l[j])
