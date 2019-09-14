l=list(map(int,input().split()))
even=[i*1 for i in l if i%2==0]
odd=[j*1 for j in l if j%2!=0]
print("Even",len(even),"\n","odd",len(odd))
