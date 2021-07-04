from math import ceil
magsquare=['']
o=input('Enter magic square size')
o=int(o)
if o%2==0:
    raise ValueError('wait what')
m=input('Enter  minimum  number ')
m=int(m)
for x in range(1, (o*o+1)):
    magsquare.append('')
def FakeArray(x, y):
    x=x-1
    s=(x*o)+y
    return s
st1=ceil(o/2)
st2=o
n=m
cpos=FakeArray(st1, st2)
def nextstep(fakearray):
    if (fakearray%o==0) and not(fakearray == o):
        return (fakearray-(2*o))+1
    elif (fakearray <= o) and not (fakearray == o):
        return ((fakearray+(o*(o-1)))+1)
    elif fakearray==o:
        return (fakearray)+(o*(o-2))+1
    else:
        return fakearray-(o-1)
for x in range(1, o*o+1):
    if magsquare[nextstep(cpos)]=='':
        magsquare[cpos]=n
        n=n+1
        cpos=nextstep(cpos)
        continue
    if not magsquare[nextstep(cpos)]=='':
        magsquare[cpos]=n
        n=n+1
        cpos=cpos-1
fmat=[]
for x in range(1, o+1):
    for y in range(1, o+1):
        fmat.append(magsquare[FakeArray(x, y)])
    print(fmat)
    fmat.clear()
magsquare.remove('')
