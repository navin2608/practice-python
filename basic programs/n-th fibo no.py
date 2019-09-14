def fib(n):
    lasttwo=[0,1]
    counter=3
    next=0
    while n>=counter:
        next=lasttwo[0]+lasttwo[1]
        lasttwo[0]=lasttwo[1]
        lasttwo[1]=next
        counter+=1
    return lasttwo[1] if n>2 else lasttwo[0]
n=int(input("enter a no"))
print(fib(n))
        
