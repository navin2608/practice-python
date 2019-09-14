st1=input()
l=list(set(st1))
su=0
a=[]
for i in l:
    a.append(st1.count(i))
ne=list(set(a))
for j in ne:
    
    su+=a.count(j)
    a.remove(j)
print(su)

    
    
    
    

