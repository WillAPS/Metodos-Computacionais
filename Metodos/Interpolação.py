



def CalcDen(v):
    D = Den = 1
    L = 0
    for j in range(len(v)):
        key = v[L]
        for i in range(len(v)):
            if i != L:
                Den = key - v[i]
                print("i -=> ", Den)
            D *= Den
        L += 1

    return D


vx = [1, 2, 3]


def printaResult(v):
    result = ""
    j = len(v) - 1
    cont = 0
    for i in range(len(v)-1, -1, -1):
        a = str(v[i])
        if cont == 1:
            result += " + "
        result += (a + j * "*x")
        cont = 1
        j -= 1
    print(result)

printaResult(vx)
