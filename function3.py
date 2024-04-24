g=[12,34,21,-12,34,55,56]
n=len(g)
target=34
result=0
for index in range(n):
    if g[index]==target:
        result=result+1
print("total number of occurances are",result)
