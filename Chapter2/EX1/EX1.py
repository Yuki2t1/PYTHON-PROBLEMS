def pgcd(x,y):
    while x!=y:
        if x>y:
            x-=y
        else:
            y-=x
    return(x)

print(pgcd(22,6))