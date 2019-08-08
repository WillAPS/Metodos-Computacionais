ERRO = 0.001
MAXREP = 10000


def Bissec(f, a, b):
    i = 1
    fa = f(a)
    while i <= MAXREP:
        # iteracao da bissecao
        p = a + (b - a) / 2
        fp = f(p)
        # condicao de parada
        if (fp == 0) or ((b - a) / 2 < ERRO):
            return p
            # bissecta o intervalo
        i = i + 1
        if fa * fp > 0:
            a = p
            fa = fp
        else:
            b = p

    raise NameError('Num.max.deiter.excedido!');