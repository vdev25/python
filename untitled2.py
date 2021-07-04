from math import floor
n=input('Enter a number')
t=''
try:
    n=int(n)
except ValueError:
    try:
        l=n.split(".")
        t=(l[1])
        n=(l[0])
        t=('.'+t)
    except ValueError:
        print('This is a string so the answer may not be what you intended...')
        t=''
n=str(n)
t=str(t)
d=''
for x in n:
    d=(x+d)
n=d
m=0
d=''
for x in n:
    m=m+1
    d=str(d+x)
    if m==3:
        d=(d+',')
        m=0
e=''
for x in d:
    e=(x+e)
if m==0:
    print((e[1:])+t)
else:
    print((e)+t)


    
        
