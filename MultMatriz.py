import math

C1L1X = 0
C2L1X = 0
C3L1X = 0
C4L1X = 0
C5L1X = 0

#termino x

C1L1Y = 0
C2L1Y = 0
C3L1Y = 0
C4L1Y = 0
C5L1Y = 0

#termino y

#============================================================================
#
#                          termino do pre defincoes
#
#============================================================================

TipoMX = input("Qual é seu tipo de Martriz X: ex(2:2) ")

if TipoMX == "1:1":
    C1L1X = input("Qual é numero na linha 1 coluna 1? ")
    print("")
    print(C1L1X)

elif TipoMX == "1:2":
    C1L1X = input("Qual é numero na linha 1 coluna 1? ")
    C2L1X = input("Qual é numero na linha 1 coluna 2? ")
    print("")
    print(C1L1X, C2L1X)

elif TipoMX == "1:3":
    C1L1X = input("Qual é numero na linha 1 coluna 1? ")
    C2L1X = input("Qual é numero na linha 1 coluna 2? ")
    C3L1X = input("Qual é numero na linha 1 coluna 3? ")
    print("")
    print(C1L1X, C2L1X, C3L1X)

elif TipoMX == "1:4":
    C1L1X = input("Qual é numero na linha 1 coluna 1? ")
    C2L1X = input("Qual é numero na linha 1 coluna 2? ")
    C3L1X = input("Qual é numero na linha 1 coluna 3? ")
    C4L1X = input("Qual é numero na linha 1 coluna 4? ")
    print("")
    print(C1L1X, C2L1X, C3L1X, C4L1X)

elif TipoMX == "1:5":
    C1L1X = input("Qual é numero na linha 1 coluna 1? ")
    C2L1X = input("Qual é numero na linha 1 coluna 2? ")
    C3L1X = input("Qual é numero na linha 1 coluna 3? ")
    C4L1X = input("Qual é numero na linha 1 coluna 4? ")
    C5L1X = input("Qual é numero na linha 1 coluna 5? ")
    print("")
    print(C1L1X, C2L1X, C3L1X, C4L1X, C5L1X)

#============================================================================
#
#                               termino do X
#
#============================================================================

TipoMY = input("Qual é seu tipo de Martriz Y:")

if TipoMY == "1:1":
    C1L1Y = input("Qual é numero na linha 1 coluna 1? ")
    print("")
    print(C1L1Y)

elif TipoMY == "1:2":
    C1L1Y = input("Qual é numero na linha 1 coluna 1? ")
    C2L1Y = input("Qual é numero na linha 1 coluna 2? ")
    print("")
    print(C1L1Y, C2L1Y)

elif TipoMY == "1:3":
    C1L1Y = input("Qual é numero na linha 1 coluna 1? ")
    C2L1Y = input("Qual é numero na linha 1 coluna 2? ")
    C3L1Y = input("Qual é numero na linha 1 coluna 3? ")
    print("")
    print(C1L1Y, C2L1Y, C3L1Y)

elif TipoMY == "1:4":
    C1L1Y = input("Qual é numero na linha 1 coluna 1? ")
    C2L1Y = input("Qual é numero na linha 1 coluna 2? ")
    C3L1Y = input("Qual é numero na linha 1 coluna 3? ")
    C4L1Y = input("Qual é numero na linha 1 coluna 4? ")
    print("")
    print(C1L1Y, C2L1Y, C3L1Y, C4L1Y)

elif TipoMY == "1:5":
    C1L1Y = input("Qual é numero na linha 1 coluna 1? ")
    C2L1Y = input("Qual é numero na linha 1 coluna 2? ")
    C3L1Y = input("Qual é numero na linha 1 coluna 3? ")
    C4L1Y = input("Qual é numero na linha 1 coluna 4? ")
    C5L1Y = input("Qual é numero na linha 1 coluna 5? ")
    print("")
    print(C1L1Y, C2L1Y, C3L1Y, C4L1Y, C5L1Y)

#============================================================================
#
#                               termino do Y
#
#============================================================================

print("")
print("Qual tipo de calculo vai utilizar: ")
print("Exemplo: multiplicacao")
Calculos = input("")

#pergunta calculo

if Calculos == "multiplicacao":
    if (TipoMX == "1:1", TipoMX == "1:1"):
        C1L1X * C1L1Y
