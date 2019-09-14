l=list(map(str,input().split()))
l1=[''.join(x for x in i if x.isalpha())for i in l]
print(l1)
