l=list(map(int,input().split()))
a=l
l2=[]
a.sort()
n=int(input())
res=[]
res=(a[:n:-1])
l2=[i*1 for i in res if i in l]
print(l2)
