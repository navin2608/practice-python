par=['()','{}','[]']
l=input()
for i in range(len


               (l)//2):
    if any(l in par):
        print('True')

print(l)
