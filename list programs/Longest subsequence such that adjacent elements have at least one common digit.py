a=list(map(int,input().split()))
co=0
for i in range(len(a)-1):
    st1=list(map(int,str(a[i])))
    st2=list(map(int,str(a[i+1])))
    if any([j in st2 for j in st1]):
        co+=1
print(co)
    
