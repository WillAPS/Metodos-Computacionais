from math import sqrt
from statistics import mean


def Correlacao_Pearson(Vx, Vy, n):
    Numerador = 0
    DenominadorX = DenominadorY = 0

    for i in range(n):
        Numerador += ((Vx[i] - mean(Vx)) * (Vy[i] - mean(Vy)))
        DenominadorX += ((Vx[i] - mean(Vx)) ** 2)
        DenominadorY += ((Vy[i] - mean(Vy)) ** 2)

    return round(Numerador/sqrt((DenominadorX * DenominadorY)), 3)


def Correlacao_Kendall(Vx, Vy, n):

    discordancia = 0
    concordancia = 0
    for i in range(n):
        for j in range(i+1, n):
            if (Vx[i] < Vx[j] and Vy[i] < Vy[j]) or (Vx[i] > Vx[j] and Vy[i] > Vy[j]):
                discordancia += 1
            else:
                concordancia += 1

    t = (discordancia - concordancia) / ((n**2 - n) / 2)

    return t


def Correlacao_Spearman(Vx, Vy, n):
    Vx.sort()
    Numerador = 0
    for i in range(n):
        Numerador += Vx[i] - Vy[i]

    return 1 - (Numerador / (n ** 3 - n))