with open('dataset_3363_2.txt') as inf:
    cod = str(inf.readline())
    dnk = ('')
    n = cod[0]
    z = ('')
    for i in range(len(cod)):
        if not cod[i].isdigit():
            n = cod[i]
        elif i + 1 < len(cod) and not cod[i+1].isdigit():
            z += cod[i]
            z = int(z)
            dnk = dnk + n * z
            z = ('')
        else:
            z += cod[i]
with open('output.txt', 'w') as ouf:
    ouf.write(dnk)
