from statistics import mean


def Tranform(string, n):
    vet = [None]*n
    string = string.split(",")
    for i in range(n):
        vet[i] = float(string[i])
    return vet


def linear(listaX, listaY, n):

    sumXY = sumX2 = 0
    listaX = Tranform(listaX, n)
    listaY = Tranform(listaY, n)

    for i in range(n):
        sumXY += listaX[i] * listaY[i]
        sumX2 += listaX[i] ** 2


    b = ((n * sumXY) - (sum(listaX) * sum(listaY))) / (n * sumX2 - sum(listaX)**2)

    a = mean(listaY) - b * mean(listaX)
    den = num = 0
    for i in range(n):
        num += (listaY[i] - ((b * listaX[i]) + a)) ** 2
        den += (listaY[i] - mean(listaY)) ** 2

    return 1 - (num/den)