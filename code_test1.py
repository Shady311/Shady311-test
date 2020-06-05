with open('dataset_3363_2.txt') as inf:
    cod = str(inf.readline())
    dnk = ('')
    i = 1
    n = cod[0]
    v = ('')
    for i in range(1, len(cod)):
        k = cod[i]
        if k.isdigit():
            v = v + k
        else:
            dnk = dnk + n * int(v)
            n = cod[i]
            v = ('')
    dnk = dnk + n * int(v)
with open('output.txt', 'w') as ouf:
    ouf.write(dnk)
