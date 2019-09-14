n1=int(input())
n2=int(input())
a=[]
a2=[]
for i in range(n1):
    l=list(map(str,input().split()))
    a.append(l)
for j in range(n2):
    l1=list(map(str,input().split()))
    a2.append(l1)
if all(k in a for k in a2):
    print("True")
else:
    print("False")
