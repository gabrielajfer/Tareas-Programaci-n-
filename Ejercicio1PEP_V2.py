##EJERCICIO 1
""" Una forma de generar numeros aleatorios es la llamada
tecnica del cuadrado medi, que consiste en tomar un número
semilla de N cifras, elevarlo al cuadrado y usar los (N) digitos
del medio como siguiente elemento al que se aplicará la misma operación
"""
semilla = input("Ingrese el número semilla: ")
oportunidades = 0

if not semilla.isnumeric():
    raise ValueError("Ingrese números")
else:
    while len(semilla) < 4 and oportunidades < 3:

        print("Debe de ser un número de 4 digitos")
        semilla = input("Ingrese el número semilla: ")
        oportunidades += 1

        if oportunidades == 2:
            print("máximo de oportunidades alcanzadas.")
            break
        if len(semilla) >= 4:
            print("Continuemos con el programa")
            break
if len(semilla) >= 4:
#Ahora Elevamos el número al cuadrado para generar números aleatorios
    print("""
        """)
    tamaño_semilla = len(semilla)
    semilla_int = int(semilla)

# "f" en python funciona para incluir varibales en su forma original dentro de un texto.
## Funciona en caso de querer imprimir muchas variables

    cuadrado = semilla_int**2
    print(f"el numero al cuadrado es: {cuadrado}")
    print("")
#Primero volvemos el cuadrado un str, para poder extraer los números del centro:

    cuadrado_str = str(cuadrado)
    longitud = len(cuadrado_str)

    """Para obtener los 4 numeros del centro debemos dividir entre 100 primero, para poder rodar la coma de derecha
a izquierda, pero en python realizamos la división entera para que luego, dividamos por 1 multiplicado por tantos
ceros para obtener los numeros del centro(En este caso 4) para ir rodando la coma hasta obtener esos numeros.
Se utiliza el operador para obtner cociente en python para obtener esos numeros.

Funciona la tecnica para tantos numeros necesite del centro, es decir, si quiero los dos del centro debo dividir
de manera entera entre 1000 y luego obtener el cociente de otra division entre 1000"""
    cuatro_del_medio = (cuadrado // 100) % 10000
    print(f"Semilla para el proximo numero: {cuatro_del_medio}")

    numero_aleatorio = cuatro_del_medio / 10000

    print(f"El número aleatorio es: {numero_aleatorio}")

#Ahora debemos incluir en un ciclo todo lo anterior planteado
    print("""
    """)
    repeticiones = int(input("Indique cuantos números aleatorios quiere generar:  "))
    print(f"""
    el nuevo número semilla es {cuatro_del_medio}
    """)

    for i in range (repeticiones):
        nuevo_cuadrado = cuatro_del_medio**2

        nueva_semilla = (nuevo_cuadrado // 100) % 10000

        nuevo_aleatorio = nueva_semilla / 10000

        print(f"El número al cuadrado es: {nuevo_cuadrado}")
        print(f"semilla: {nueva_semilla}; numero aleatorio: {nuevo_aleatorio}")

        print("""
    """)
        cuatro_del_medio = nueva_semilla