n = input('Enter a number')
try:
    n=int(n)
    valid=True
except ValueError:
    print('This is a string/float and cannot be processed.')
    valid=False
mysum = 0

negative = False
if n < 0:
    n = -n
    negative = True
if valid:
    for counter in range(1,n+1):
        mysum=counter+mysum
        counter=counter+1

if negative:
    print(-mysum)
else:
    print(mysum)
