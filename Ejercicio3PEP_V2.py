##EJERCICIO 3: LA MATRIZ DE MxN

#Pedimos al usuario el numero de filas y columnas de la matriz

n = int(input("diga el numero de filas: "))
m = int(input("diga el numero de columnas: "))

if (type(m) == str or type(n) == str):
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
    #para las filas impares que representan las filas pares de la matriz, haremos que se inviertan los valor usando el metodo reversed

    for z in range (n):
        if z % 2 == 1:
            matriz[z]= list(reversed(matriz[z]))

    #Ahora imprimo en forma de matriz
    b = 0
    for i in range (n):
        print(f"{matriz[b]}")
        b += 1