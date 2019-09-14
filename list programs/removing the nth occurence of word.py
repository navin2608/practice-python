a=list(map(str,input("enter the array of words\n").split()))
word=input("enter the word to be removed \n")
n=int(input("enter the nth occurence\n"))
co=0
for i in range(len(a)):
    if a[i]==word:
        co+=1
        if co==n:
            a.pop(i)
            break
print("resultant array",a)
