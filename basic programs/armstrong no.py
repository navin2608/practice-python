a=input("enter a no")
tot=0
for i in a:
    i=int(i)
    tot+=(i)**3
if(str(tot)==a):
    print("its an armstrong no")
else:
    print("not an armstrong no")
