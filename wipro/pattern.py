n=int(input())
columns=0
center=0
if (n%2==0):
    columns=n+1
else:
    columns=n
row=n+1
for i in range(row):
    for j in range(columns):
        if (i>0 and j==(columns//2)):
            center+=1
            print(center,end=" ")
        else:
            print(n,end=" ")
    print("")
