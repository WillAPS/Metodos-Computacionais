def CalcNum():
    cont = 0
    vx = [1, 2, 3, 4]
    result = ""
    for i in range(len(vx) - 1):
        if cont == 1:
            result += "*"
            cont = 0
        result += "x"
        cont += 1
    print(result)


def CalcDen(L):
    D = 1
    Den = 1
    vx = [1, 2, 3]
    vy = [1, 2, 3]
    key = vx[L]
    for i in range(3):
        if i != L:
            Den = key - vx[i]
        D *= Den

    print(D)


CalcNum()


