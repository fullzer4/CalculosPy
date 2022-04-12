import numpy as np

Matriz1 = input("Qual o tipo da sua 1 matriz: ex(2:2) ")
Matriz2 = input("Qual o tipo da sua 2 matriz: ex(2:2) ")
print("")

if Matriz1 == "2:2":
    print("Matriz 1")
    print("")
    C1L1X= int(input("Coluna 1 Linha 1: "))
    C2L1X= int(input("Coluna 2 Linha 1: "))
    C1L2X= int(input("Coluna 1 Linha 2: "))
    C2L2X= int(input("Coluna 2 Linha 2: "))
    print("")
    M1a = np.array([[C1L1X, C2L1X],
    [C1L2X, C2L2X]])

    if Matriz2 == "2:2":
        print("Matriz 2")
        print("")
        C1L1Y= int(input("Coluna 1 Linha 1: "))
        C2L1Y= int(input("Coluna 2 Linha 1: "))
        C1L2Y= int(input("Coluna 1 Linha 2: "))
        C2L2Y= int(input("Coluna 2 Linha 2: "))
        print("")
        M2a = np.array([[C1L1Y, C2L1Y],
        [C1L2Y, C2L2Y]])

    elif Matriz2 == "2:3":
        print("Matriz 2")
        print("")
        C1L1Y= int(input("Coluna 1 Linha 1: "))
        C2L1Y= int(input("Coluna 2 Linha 1: "))
        C1L2Y= int(input("Coluna 1 Linha 2: "))
        C2L2Y= int(input("Coluna 2 Linha 2: "))
        C1L3Y= int(input("Coluna 1 Linha 3: "))
        C2L3Y= int(input("Coluna 2 Linha 3: "))
        print("")
        M2a = np.array([[C1L1Y, C2L1Y],
        [C1L2Y, C2L2Y],
        [C1L3Y, C2L3Y]])

    elif Matriz2 == "2:4":
        print("Matriz 2")
        print("")
        C1L1Y= int(input("Coluna 1 Linha 1: "))
        C2L1Y= int(input("Coluna 2 Linha 1: "))
        C1L2Y= int(input("Coluna 1 Linha 2: "))
        C2L2Y= int(input("Coluna 2 Linha 2: "))
        C1L3Y= int(input("Coluna 1 Linha 3: "))
        C2L3Y= int(input("Coluna 2 Linha 3: "))
        C1L4Y= int(input("Coluna 1 Linha 4: "))
        C2L4Y= int(input("Coluna 2 Linha 4: "))
        print("")
        M2a = np.array([[C1L1Y, C2L1Y],
        [C1L2Y, C2L2Y],
        [C1L3Y, C2L3Y],
        [C1L4Y, C2L4Y]])

    elif Matriz2 == "2:5":
        print("Matriz 2")
        print("")
        C1L1Y= int(input("Coluna 1 Linha 1: "))
        C2L1Y= int(input("Coluna 2 Linha 1: "))
        C1L2Y= int(input("Coluna 1 Linha 2: "))
        C2L2Y= int(input("Coluna 2 Linha 2: "))
        C1L3Y= int(input("Coluna 1 Linha 3: "))
        C2L3Y= int(input("Coluna 2 Linha 3: "))
        C1L4Y= int(input("Coluna 1 Linha 4: "))
        C2L4Y= int(input("Coluna 2 Linha 4: "))
        C1L5Y= int(input("Coluna 1 Linha 5: "))
        C2L5Y= int(input("Coluna 2 Linha 5: "))
        print("")
        M2a = np.array([[C1L1Y, C2L1Y],
        [C1L2Y, C2L2Y],
        [C1L3Y, C2L3Y],
        [C1L4Y, C2L4Y],
        [C1L5Y, C2L5Y]])
        
    elif Matriz2 == "2:6":
        print("Matriz 2")
        print("")
        C1L1Y= int(input("Coluna 1 Linha 1: "))
        C2L1Y= int(input("Coluna 2 Linha 1: "))
        C1L2Y= int(input("Coluna 1 Linha 2: "))
        C2L2Y= int(input("Coluna 2 Linha 2: "))
        C1L3Y= int(input("Coluna 1 Linha 3: "))
        C2L3Y= int(input("Coluna 2 Linha 3: "))
        C1L4Y= int(input("Coluna 1 Linha 4: "))
        C2L4Y= int(input("Coluna 2 Linha 4: "))
        C1L5Y= int(input("Coluna 1 Linha 5: "))
        C2L5Y= int(input("Coluna 2 Linha 5: "))
        C1L6Y= int(input("Coluna 1 Linha 6: "))
        C2L6Y= int(input("Coluna 2 Linha 6: "))
        print("")
        M2a = np.array([[C1L1Y, C2L1Y],
        [C1L2Y, C2L2Y],
        [C1L3Y, C2L3Y],
        [C1L4Y, C2L4Y],
        [C1L5Y, C2L5Y],
        [C1L6Y, C2L6Y]])
        
    elif Matriz2 == "2:7":
        print("Matriz 2")
        print("")
        C1L1Y= int(input("Coluna 1 Linha 1: "))
        C2L1Y= int(input("Coluna 2 Linha 1: "))
        C1L2Y= int(input("Coluna 1 Linha 2: "))
        C2L2Y= int(input("Coluna 2 Linha 2: "))
        C1L3Y= int(input("Coluna 1 Linha 3: "))
        C2L3Y= int(input("Coluna 2 Linha 3: "))
        C1L4Y= int(input("Coluna 1 Linha 4: "))
        C2L4Y= int(input("Coluna 2 Linha 4: "))
        C1L5Y= int(input("Coluna 1 Linha 5: "))
        C2L5Y= int(input("Coluna 2 Linha 5: "))
        C1L6Y= int(input("Coluna 1 Linha 6: "))
        C2L6Y= int(input("Coluna 2 Linha 6: "))
        C1L7Y= int(input("Coluna 1 Linha 7: "))
        C2L7Y= int(input("Coluna 2 Linha 7: "))
        print("")
        M2a = np.array([[C1L1Y, C2L1Y],
        [C1L2Y, C2L2Y],
        [C1L3Y, C2L3Y],
        [C1L4Y, C2L4Y],
        [C1L5Y, C2L5Y],
        [C1L6Y, C2L6Y],
        [C1L7Y, C2L7Y]])
        
    elif Matriz2 == "2:8":
        print("Matriz 2")
        print("")
        C1L1Y= int(input("Coluna 1 Linha 1: "))
        C2L1Y= int(input("Coluna 2 Linha 1: "))
        C1L2Y= int(input("Coluna 1 Linha 2: "))
        C2L2Y= int(input("Coluna 2 Linha 2: "))
        C1L3Y= int(input("Coluna 1 Linha 3: "))
        C2L3Y= int(input("Coluna 2 Linha 3: "))
        C1L4Y= int(input("Coluna 1 Linha 4: "))
        C2L4Y= int(input("Coluna 2 Linha 4: "))
        C1L5Y= int(input("Coluna 1 Linha 5: "))
        C2L5Y= int(input("Coluna 2 Linha 5: "))
        C1L6Y= int(input("Coluna 1 Linha 6: "))
        C2L6Y= int(input("Coluna 2 Linha 6: "))
        C1L7Y= int(input("Coluna 1 Linha 7: "))
        C2L7Y= int(input("Coluna 2 Linha 7: "))
        C1L8Y= int(input("Coluna 1 Linha 8: "))
        C2L8Y= int(input("Coluna 2 Linha 8: "))
        print("")
        M2a = np.array([[C1L1Y, C2L1Y],
        [C1L2Y, C2L2Y],
        [C1L3Y, C2L3Y],
        [C1L4Y, C2L4Y],
        [C1L5Y, C2L5Y],
        [C1L6Y, C2L6Y],
        [C1L7Y, C2L7Y],
        [C1L8Y, C2L8Y]])
        
    elif Matriz2 == "2:9":
        print("Matriz 2")
        print("")
        C1L1Y= int(input("Coluna 1 Linha 1: "))
        C2L1Y= int(input("Coluna 2 Linha 1: "))
        C1L2Y= int(input("Coluna 1 Linha 2: "))
        C2L2Y= int(input("Coluna 2 Linha 2: "))
        C1L3Y= int(input("Coluna 1 Linha 3: "))
        C2L3Y= int(input("Coluna 2 Linha 3: "))
        C1L4Y= int(input("Coluna 1 Linha 4: "))
        C2L4Y= int(input("Coluna 2 Linha 4: "))
        C1L5Y= int(input("Coluna 1 Linha 5: "))
        C2L5Y= int(input("Coluna 2 Linha 5: "))
        C1L6Y= int(input("Coluna 1 Linha 6: "))
        C2L6Y= int(input("Coluna 2 Linha 6: "))
        C1L7Y= int(input("Coluna 1 Linha 7: "))
        C2L7Y= int(input("Coluna 2 Linha 7: "))
        C1L8Y= int(input("Coluna 1 Linha 8: "))
        C2L8Y= int(input("Coluna 2 Linha 8: "))
        C1L9Y= int(input("Coluna 1 Linha 9: "))
        C2L9Y= int(input("Coluna 2 Linha 9: "))
        print("")
        M2a = np.array([[C1L1Y, C2L1Y],
        [C1L2Y, C2L2Y],
        [C1L3Y, C2L3Y],
        [C1L4Y, C2L4Y],
        [C1L5Y, C2L5Y],
        [C1L6Y, C2L6Y],
        [C1L7Y, C2L7Y],
        [C1L8Y, C2L8Y],
        [C1L9Y, C2L9Y]])
        
    elif Matriz2 == "2:10":
        print("Matriz 2")
        print("")
        C1L1Y= int(input("Coluna 1 Linha 1: "))
        C2L1Y= int(input("Coluna 2 Linha 1: "))
        C1L2Y= int(input("Coluna 1 Linha 2: "))
        C2L2Y= int(input("Coluna 2 Linha 2: "))
        C1L3Y= int(input("Coluna 1 Linha 3: "))
        C2L3Y= int(input("Coluna 2 Linha 3: "))
        C1L4Y= int(input("Coluna 1 Linha 4: "))
        C2L4Y= int(input("Coluna 2 Linha 4: "))
        C1L5Y= int(input("Coluna 1 Linha 5: "))
        C2L5Y= int(input("Coluna 2 Linha 5: "))
        C1L6Y= int(input("Coluna 1 Linha 6: "))
        C2L6Y= int(input("Coluna 2 Linha 6: "))
        C1L7Y= int(input("Coluna 1 Linha 7: "))
        C2L7Y= int(input("Coluna 2 Linha 7: "))
        C1L8Y= int(input("Coluna 1 Linha 8: "))
        C2L8Y= int(input("Coluna 2 Linha 8: "))
        C1L9Y= int(input("Coluna 1 Linha 9: "))
        C2L9Y= int(input("Coluna 2 Linha 9: "))
        C1L10Y= int(input("Coluna 1 Linha 10: "))
        C2L10Y= int(input("Coluna 2 Linha 10: "))
        print("")
        M2a = np.array([[C1L1Y, C2L1Y],
        [C1L2Y, C2L2Y],
        [C1L3Y, C2L3Y],
        [C1L4Y, C2L4Y],
        [C1L5Y, C2L5Y],
        [C1L6Y, C2L6Y],
        [C1L7Y, C2L7Y],
        [C1L8Y, C2L8Y],
        [C1L9Y, C2L9Y],
        [C1L10Y, C2L10Y]])

print(M1a @ M2a)

#a fazer ainda 2:2 * 2:3 para cima