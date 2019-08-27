from math import sqrt
from statistics import mean


def Tranform(string, n):
    vet = [None]*n
    string = string.split(",")
    for i in range(n):
        vet[i] = float(string[i])
    return vet


def Correlacao_Pearson(Vx, Vy, n):
    vx = Tranform(Vx, n)
    vy = Tranform(Vy, n)
    Numerador = 0
    DenominadorX = DenominadorY = 0

    for i in range(n):
        Numerador += ((vx[i] - mean(vx)) * (vy[i] - mean(vy)))
        DenominadorX += ((vx[i] - mean(vx)) ** 2)
        DenominadorY += ((vy[i] - mean(vy)) ** 2)

    return round(Numerador/sqrt((DenominadorX * DenominadorY)), 3)


def Correlacao_Kendall(Vx, Vy, n):
    Vx = Tranform(Vx, n)
    Vy = Tranform(Vy, n)
    discordancia = 0
    concordancia = 0
    for i in range(n):
        for j in range(i+1, n):
            if (Vx[i] < Vx[j] and Vy[i] < Vy[j]) or (Vx[i] > Vx[j] and Vy[i] > Vy[j]):
                discordancia += 1
            else:
                concordancia += 1

    t = (concordancia - discordancia) / ((n**2 - n) / 2)

    return t


def Correlacao_Spearman(Vx, Vy, n):
    Vx = Tranform(Vx, n)
    Vy = Tranform(Vy, n)
    Vx.sort()
    Numerador = 0
    for i in range(n):
        Numerador += Vx[i] - Vy[i]

    return 1 - (6*Numerador / (n ** 3 - n))