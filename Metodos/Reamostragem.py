from random import randint
from statistics import mean


def bootstrap(v, rep, n):

    aux = [0]*rep
    s = 0
    for i in range(rep):
        for j in range(n):
            indice = randint(0, n-1)
            s += v[indice]
        aux[i] = s/n
        s = 0

    return mean(v), mean(aux)


def jackknife(v, n):

    aux = [0] * n
    for i in range(n):
        aux[i] = (sum(v) - v[i]) / n


    return mean(v), mean(aux)
