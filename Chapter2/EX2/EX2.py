def ppcm(x,y):
    i=1
    r=x*i
    while r%y!=0:
        i+=1
        r=x*i
    return(r)

print(ppcm(168,36))
