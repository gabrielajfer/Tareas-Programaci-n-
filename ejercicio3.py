##EJERCICIO 3: LA MATRIZ DE MxN

#Pedimos al usuario el numero de filas y columnas de la matriz

n = int(input("diga el numero de filas: "))
m = int(input("diga el numero de columnas: "))

if (m == str or n == str):
    print("Ingrese datos numericos.")

else:
    #Establezco la matriz
    matriz = []

    #Con la operacion append * n agrego las columnas al numero de filas
    #establezco un contador para imprimir una matriz de 0

    a=0
    for i in range (n):
        matriz.append([a] * m)

    #primero establezco una matriz de ceros, luego agrego los valores:
    for i in range(n):
        for j in range (m):
            a += 1
            matriz[i][j] = a

    #Ahora imprimo en forma de matriz
    b = 0
    for i in range (n):
        print(f"{matriz[b]}")
        b += 1