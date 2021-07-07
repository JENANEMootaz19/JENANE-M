def maximum(a,b,c):
    if a>=b and a>=c:
        largest= a
    elif b>=a and b>=c:
        largest= b
    else:
        largest= c
    return largest

print( maximum(25,23,11))
