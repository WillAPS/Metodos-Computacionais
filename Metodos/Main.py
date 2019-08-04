import Intervalo_Confiança
import Coeficiente_Correlação
import Reamostragem
import Interpolacao

TypeMetodo = int(input("[1] = Intervalo de confiança\n"
                       "[2] = Coeficiente de Correlação\n"
                       "[3] = Reamostragem\n"
                       "[4] = Interpolação\n"
                       "=> "))

if TypeMetodo == 1:
    Metodo = int(input("Metodo Desejado \n"
                       "[1] = Media Conhecida\n"
                       "[2] = Media Populacional\n"
                       "[3] = Media Amostral\n"
                       "=> "))

    nivel_confianca = float(input("Nivel de Confiança => "))
    quant_dados = int(input("Quant Valores => "))

    if (Metodo == 1) or (Metodo == 3):
        media = float(input("Insira a media -> "))
        desvio_padrao = float(input("Desvio padrao => "))
        if Metodo == 1:
            IC = Intervalo_Confiança.MediaConhecida(media, quant_dados, desvio_padrao, nivel_confianca)
        else:
            IC = Intervalo_Confiança.Amostra(media, quant_dados, desvio_padrao, nivel_confianca)

    elif Metodo == 3:
        sucesso_dados = int(input("Amostra de Sucesso => "))
        IC = Intervalo_Confiança.MediaPopulacional(quant_dados, nivel_confianca, sucesso_dados)

    print("Intervalo de Confiança => ", IC)

if TypeMetodo == 2:
    Correlacao = int(input("Correlacao Desejada\n"
                           "[1] = Pearson\n"
                           "[2] = Spearman\n"
                           "[3] = Kendall\n"
                           "=> "))
    quant_dados = int(input("Quant Dados => "))
    Vx = [None] * quant_dados
    Vy = [None] * quant_dados
    for i in range(quant_dados):
        Vx[i] = float(input("Valores de X => "))
    for i in range(quant_dados):
        Vy[i] = float(input("Valores de Y => "))

    if Correlacao == 1:
        p = Coeficiente_Correlação.Correlacao_Pearson(Vx, Vy, quant_dados)

    if Correlacao == 2:
        p = Coeficiente_Correlação.Correlacao_Spearman(Vx, Vy, quant_dados)

    if Correlacao == 3:
        p = Coeficiente_Correlação.Correlacao_Kendall(Vx, Vy, quant_dados)

    print("Nivel Correlacao => ", p)

if TypeMetodo == 3:
    Reamostrage = int(input("[1] = Bootstrap\n"
                            "[2] = Jackknife\n"
                            "=> "))
    n = int(input("Quant de dados => "))
    v = [None] * n

    for i in range(n):
        v[i] = float(input("Insira o valor => "))


    if Reamostrage == 1:
        rep = int(input("Quant de repeticoes => "))
        b = Reamostragem.bootstrap(v, rep, n)
        print("Estimativa normal e com Bootstrap => ", b)

    if Reamostrage == 2:
        j = Reamostragem.jackknife(v, n)
        print("Estimativa normal e com Jackkife => ", j)

if TypeMetodo == 4:




