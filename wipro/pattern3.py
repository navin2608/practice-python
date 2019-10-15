string=input()
vow=['a','e','i','o','u','A','E','I','O','U']
final=[]
for i in string:
    if i not in vow:
        final.append(i)
print("".join(s for s in final))
        
