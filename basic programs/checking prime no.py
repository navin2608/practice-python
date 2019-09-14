import timeit

a=int(input("enter a no"))
'''
if(a>2):
    for i in range(2,a):
        if a%i==0:
            print("not a prime no")
            break
    else:
        print("its an prime no")
elif a==0 or 1:
    print("its a prime no")
'''
c=0
for i in range(2,a//2+1):
    if a%i==0:
        c+=1
if c>0:
    print("not prime")
else:
    print("prime")
    #'''
    
print(timeit.timeit())
