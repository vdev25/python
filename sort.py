i=''
l=[]
while True:
    i=input()
    try:
        i=int(i)
    except ValueError:
        print('This is a string. Enter a positive integer to continue or a negative integer to stop.')
        i=''
        continue
    if i>=0:
        l.append(i)
    else:
        break
def swap(i1, i2):
    c1=l[i1]
    c2=l[i2]
    l[i1]=c2
    l[i2]=c1
ind1=0
ind2=1
correctcount=0
try:
    while not(correctcount==(len(l))):
        correctcount=0
        if (l[ind1] > l[ind2]):
            swap(ind1, ind2)
            correctcount=0
            ind1=0
            ind2=1
            continue
        else:
            ind1=ind1+1
            ind2=ind2+1
            correctcount=correctcount+1
            if correctcount==(len(l)):
                break
except IndexError:
    print(l)
