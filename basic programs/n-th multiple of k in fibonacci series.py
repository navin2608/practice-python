def fib(n):
    lasttwo=[0,1]
    next=0
    counter=3
    l=[]
    l.append(lasttwo[0])
    l.append(lasttwo[1])
    while counter<=n:
        next=lasttwo[0]+lasttwo[1]
        lasttwo[0]=lasttwo[1]
        lasttwo[1]=next
        counter+=1
        l.append(lasttwo[1])
    return l
n=int(input("enter n th multiple"))
k=int(input("enter the muliplier"))
val=fib(100)
ex=[i*1 for i in val if i%k==0]
print(ex[n])
print("position",val.index(ex[n]))

