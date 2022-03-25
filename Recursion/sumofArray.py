def sumArray(a):
    l=len(a)
    if l==0:
        return 0
    if l==1:
        return a[0]
    smaller=a[1:]
    out=sumArray(smaller)
    return a[0]+out
a=[30,20,-10,10]
print(sumArray(a))