def fib(n):
    lasttwo=[0,1]
    counter=3
    next=0
    ap=[]
    ap.append(lasttwo[0])
    ap.append(lasttwo[1])
    while n>=counter:
        next=lasttwo[0]+lasttwo[1]
        lasttwo[0]=lasttwo[1]
        lasttwo[1]=next
        counter+=1
        ap.append(lasttwo[1])
    return ap 
n=int(input("enter a no"))
print(fib(n))
        
