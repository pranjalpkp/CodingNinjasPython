def powerNumber(a,b):
    if b==1:
        return a
    if b==0:
        return 1
    smallerOutput=powerNumber(a,b-1)
    return a*smallerOutput
a=2
b=5
print(powerNumber(a,b))