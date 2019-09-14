l=list(map(int,input().split()))
de=list(map(int,input().split()))
any([(i in l,l.remove(i)) for i in de])
  
print(l)
