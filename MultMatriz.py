TipoMatrizX = (input("Qual e seu tipo de matriz x? (ex 2:2): "))

if TipoMatrizX == "1:1":
    Col1Lin1x = int(input("Qual e o numero da linha 1 coluna 1: "))
    print(Col1Lin1x)
    print("")

elif TipoMatrizX == "1:2":
    Col1Lin1x = int(input("Qual e o numero da linha 1 coluna 1: "))
    Col2Lin1x = int(input("Qual e o numero da linha 1 coluna 2: "))
    print(Col1Lin1x, Col2Lin1x)
    print("")

elif TipoMatrizX == "1:3":
    Col1Lin1x = int(input("Qual e o numero da linha 1 coluna 1: "))
    Col2Lin1x = int(input("Qual e o numero da linha 1 coluna 2: "))
    Col3Lin1x = int(input("Qual e o numero da linha 1 coluna 3: "))
    print(Col1Lin1, Col2Lin1, Col3Lin1)
    print("")

elif TipoMatrizX == "2:1":
    Col1Lin1x = int(input("Qual e o numero da linha 1 coluna 1: "))
    Col1Lin2x = int(input("Qual e o numero da linha 1 coluna 2: "))
    print(Col1Lin1x, Col1Lin2x)
    print("")

elif TipoMatrizX == "2:2":
    Col1Lin1x = int(input("Qual e o numero da linha 1 coluna 1: "))
    Col2Lin1x = int(input("Qual e o numero da linha 1 coluna 2: "))
    Col1Lin2x = int(input("Qual e o numero da linha 2 coluna 1: "))
    Col2Lin2x = int(input("Qual e o numero da linha 2 coluna 2: "))
    print(Col1Lin1x, Col2Lin1x)
    print(Col1Lin2x, Col2Lin2x)
    print("") #arrumado

elif TipoMatrizX == "2:3":
    Col1Lin1x = int(input("Qual e o numero da linha 1 coluna 1: "))
    Col1Lin2x = int(input("Qual e o numero da linha 1 coluna 2: "))
    Col2Lin1x = int(input("Qual e o numero da linha 2 coluna 1: "))
    Col2Lin2x = int(input("Qual e o numero da linha 2 coluna 2: "))
    Col3Lin1x = int(input("Qual e o numero da linha 2 coluna 1: "))
    Col3Lin2x = int(input("Qual e o numero da linha 2 coluna 2: "))
    print(Col1Lin1x, Col1Lin2x, Col2Lin1x, Col2Lin2x, Col3Lin1x, Col3Lin2x)
    print("")

#ate aqui Tipo de Matriz X

TipoMatrizY = (input("Qual e seu tipo de matriz y? (ex 2:2): "))

if TipoMatrizY == "1:1":
    Col1Lin1y = int(input("Qual e o numero da linha 1 coluna 1: "))
    print(Col1Lin1y)
    print("")

elif TipoMatrizY == "1:2":
    Col1Lin1y = int(input("Qual e o numero da linha 1 coluna 1: "))
    Col2Lin1y = int(input("Qual e o numero da linha 1 coluna 2: "))
    print(Col1Lin1y, Col2Lin1y)
    print("")

elif TipoMatrizY == "1:3":
    Col1Lin1y = int(input("Qual e o numero da linha 1 coluna 1: "))
    Col2Lin1y = int(input("Qual e o numero da linha 1 coluna 2: "))
    Col3Lin1y = int(input("Qual e o numero da linha 1 coluna 3: "))
    print(Col1Lin1y, Col2Lin1y, Col3Lin1y)
    print("")

elif TipoMatrizY == "2:1":
    Col1Lin1y = int(input("Qual e o numero da linha 1 coluna 1: "))
    Col1Lin2y = int(input("Qual e o numero da linha 1 coluna 2: "))
    print(Col1Lin1y, Col1Lin2y)
    print("")

elif TipoMatrizY == "2:2":
    Col1Lin1y = int(input("Qual e o numero da linha 1 coluna 1: "))
    Col2Lin1y = int(input("Qual e o numero da linha 1 coluna 2: "))
    Col1Lin2y = int(input("Qual e o numero da linha 2 coluna 1: "))
    Col2Lin2y = int(input("Qual e o numero da linha 2 coluna 2: "))
    print(Col1Lin1y, Col2Lin1y)
    print(Col1Lin2y, Col2Lin2y)
    print("") #arrumado

elif TipoMatrizY == "2:3":
    Col1Lin1y = int(input("Qual e o numero da linha 1 coluna 1: "))
    Col1Lin2y = int(input("Qual e o numero da linha 1 coluna 2: "))
    Col2Lin1y = int(input("Qual e o numero da linha 2 coluna 1: "))
    Col2Lin2y = int(input("Qual e o numero da linha 2 coluna 2: "))
    Col3Lin1y = int(input("Qual e o numero da linha 2 coluna 1: "))
    Col3Lin2y = int(input("Qual e o numero da linha 2 coluna 2: "))
    print(Col1Lin1y, Col1Lin2y, Col2Lin1y, Col2Lin2y, Col3Lin1y, Col3Lin2y)
    print("")

#ate aqui Tipo de Matriz Y

print("Escolha o Tipo de calculo exemplos:")
print("multiplicacao")
print("")
Calculos = (input(""))

if Calculos == "multiplicacao":
    if (TipoMatrizX == "2:2", TipoMatrizY == "2:2"):
        Col1Lin1semi1 = Col1Lin1x * Col1Lin1y
        Col1Lin1semi2 = Col2Lin1x * Col1Lin2y
        Col1Lin1Total = Col1Lin1semi1 + Col1Lin1semi2

        #Col1Lin2semi1 = 
        #Col1Lin2semi2 = 
        #Col1Lin2Total = 

        Col2Lin1semi1 = Col1Lin2x * Col2Lin1y
        Col2Lin1semi2 = Col2Lin2x * Col2Lin2y
        Col2Lin1Total = Col2Lin1semi1 + Col2Lin1semi2
        Total = print(Col1Lin1Total)
        Total = print(Col2Lin1Total)

