from math import ceil

magsquare = ['']
orde = input('Enter magic square size')
orde = int(orde)


def nextstep(fakearray):
    if (fakearray % orde == 0) and not (fakearray == orde):
        return (fakearray - (2 * orde)) + 1
    elif (fakearray <= orde) and not (fakearray == orde):
        return (fakearray + (orde * (orde - 1))) + 1
    elif fakearray == orde:
        return fakearray + (orde * (orde - 2)) + 1
    else:
        return fakearray - (orde - 1)


def FakeArray(x, y, order):
    x = x - 1
    s = (x * order) + y
    return s


def space(n):
    n = str(n)


def listswap(p1, p2):
    b = p2
    magsquaree[p1 - 1] = p2
    magsquaree[b - 1] = p1


def listswap2(p1, p2):
    b = p2
    save = magsquareo3[p1 - 1]
    magsquareo3[p1 - 1] = magsquareo3[p2 - 1]
    magsquareo3[b - 1] = save


def magsquareodd(o, m):
    orde = o
    magsquare = ['']
    for x in range(1, (o * o + 1)):
        magsquare.append('')
    st1 = ceil(o / 2)
    st2 = o
    n = m
    maxl = 0
    cpos = FakeArray(st1, st2, o)
    for x in str((o * o) + n):
        maxl = maxl + 1
    for x in range(1, o * o + 1):
        if magsquare[nextstep(cpos)] == '':
            magsquare[cpos] = n
            n = n + 1
            cpos = nextstep(cpos)
            continue
        if not magsquare[nextstep(cpos)] == '':
            magsquare[cpos] = n
            n = n + 1
            cpos = cpos - 1
    fmat = []
    for x in range(1, o + 1):
        for y in range(1, o + 1):
            fmat.append(magsquare[FakeArray(x, y, o)])
        print(fmat)
        fmat.clear()


def magsquareven(oe):
    magsquaree = []
    for x in range(1, oe * oe + 1):
        magsquaree.append(x)
    switsquares = []
    for x in range(0, int(oe / 4)):
        for y in range(((x * oe) + 1), ((int(oe / 4)) + x * oe) + 1):
            switsquares.append(y)
    evenoff = int((3 / 4) * oe)
    for x in range(0, int(oe / 4)):
        for y in range(x * oe + evenoff + 1, int(oe / 4) + x * oe + evenoff + 1):
            switsquares.append(y)
    quarsq = int(oe * oe / 4)
    for x in range(0, int(oe / 4)):
        for y in range(quarsq + int(oe / 4) + 1 + x * oe, quarsq + evenoff + 1 + x * oe):
            switsquares.append(y)
    b = int(0)

    def listswap(p1, p2):
        b = p2
        magsquaree[p1 - 1] = p2
        magsquaree[b - 1] = p1

    for x in switsquares:
        listswap(x, ((oe * oe) + 1) - x)
    formatl = []
    c = 0
    for x in magsquaree:
        formatl.append(x)
        c = c + 1
        if c % oe == 0:
            print(formatl)
            c = 0
            formatl.clear()


def magsquareoddret(o, m):
    orde = o
    magsquare = ['']
    for x in range(1, (o * o + 1)):
        magsquare.append('')
    st1 = ceil(o / 2)
    st2 = o
    n = m
    maxl = 0
    cpos = FakeArray(st1, st2, o)
    for x in str((o * o) + n):
        maxl = maxl + 1
    for x in range(1, o * o + 1):
        if magsquare[nextstep(cpos)] == '':
            magsquare[cpos] = n
            n = n + 1
            cpos = nextstep(cpos)
            continue
        if not magsquare[nextstep(cpos)] == '':
            magsquare[cpos] = n
            n = n + 1
            cpos = cpos - 1
    magsquare.remove('')
    return magsquare


def magsquareoe(od):
    global magsquareo3
    magsquareo3 = []
    count = 0
    row = 0
    ho = int(od / 2)
    orde = ho
    sq1 = magsquareoddret(int(ho), 1)
    sq2 = magsquareoddret(int(ho), int((od * od * 1 / 2) + 1))
    sq3 = magsquareoddret(int(ho), int((od * od * 3 / 4) + 1))
    sq4 = magsquareoddret(int(ho), int((od * od * 1 / 4) + 1))
    orde = orde * 2
    qo = ceil(ho / 2)
    for x in range(1, ho + 1):
        for y in range(1, od + 1):
            count = count + 1
            if count > ho:
                magsquareo3.append(sq2[(count - ho) + (row * ho) - 1])
            else:
                magsquareo3.append(sq1[count + (row * ho) - 1])
        count = 0
        row = row + 1
    row = 0
    for x in range(1, ho + 1):
        for y in range(1, od + 1):
            count = count + 1
            if count > ho:
                magsquareo3.append(sq4[(count - ho) + (row * ho) - 1])
            else:
                magsquareo3.append(sq3[count + (row * ho) - 1])
        count = 0
        row = row + 1
    global switchsquare
    switchsquare = []
    global switchsquare2
    switchsquare2 = []
    for x in range(1, ho + 1):
        for y in range(1, qo):
            switchsquare.append(FakeArray(x, y, od))
    switchsquare.append(FakeArray(qo, qo, od))
    for x in switchsquare:
        switchsquare2.append(x + (int(od * od / 2)))
    switchsquare.pop((qo * (qo - 1)) - 1)
    switchsquare2.pop((qo * (qo - 1)) - 1)
    for x in range(0, (len(switchsquare))):
        listswap2(switchsquare[x], switchsquare2[x])
    fmat = []
    for x in range(0, od):
        for y in range(0, od):
            # print(magsquareo3[((x*od)+y)])
            fmat.append(magsquareo3[((x * od) + y)])
        print(fmat)
        fmat.clear()


if orde % 2 == 1:
    magsquareodd(orde, 1)
elif orde == 2:
    print('Magic square of order 2 is invalid')
elif orde % 4 == 0:
    magsquareven(orde)
else:
    orde = int(orde / 2)
    magsquareoe(orde * 2)
