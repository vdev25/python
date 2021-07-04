from math import floor
n=input('Enter an integer')
string=0
try:
    n=int(n)
except ValueError:
    print('This is a string, which cannot be processed.')
    string=1
if string==0:
    n=str(n)
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

    if (len(e)%3) == 0:
        print ((e[1:]))
    else:
        print ((e))
# comment- string reversal function
    # meaningful variable names
    # loop - do you want to continue
    
