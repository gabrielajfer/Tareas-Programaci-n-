# Tenemos la opción 0 y la lista vacía para poder ingresar al supermercado.
# Creamos una lista vacía que será el carrito, al cual se le añadirán productos.

opcion = 0
inventario = []
carrito = []

print("""BIENVENIDO AL SISTEMA DE CENTRAL MADEIRENSE

""")

while opcion != 1 and opcion != 2:
    print("""Marque 1 si es empleado
Marque 2 si es cliente
Marque 3 para salir: 
""")
    opcion = int(input("Ingrese su opción: "))

    if opcion < 0 or opcion > 2:
        print("Ingrese un valor válido.")

while opcion != 0:
    if opcion == 1:
        print("Sistema de empleados.")
        contraseña_correcta = "1234"
        intentos = 0

        while intentos < 3:
            contrasena = input("Ingrese la contraseña: ")
            if contrasena != contraseña_correcta:
                print("Contraseña incorrecta.")
                intentos += 1
            else:
                print("Contraseña correcta. Acceso concedido.")
                break

        if intentos == 3:
            print("Demasiados intentos. Acceso denegado.")
            break
#Ingresamos los datos del producto, los agregamos a un diccionario y lo añadimos al inventario.

        producto = input("Ingrese el producto: ")
        print()
        precio = float(input("Ingrese el precio: "))
        print()
        cantidad = int(input("Ingrese la cantidad: "))
        print()

        datos_producto = {
            "Producto": producto,
            "Precio": precio,
            "Cantidad": cantidad,
        }

        print(f"Entro al sistema {datos_producto['Producto']}")
        print(f"Vale {datos_producto['Precio']}$")
        print(f"Llegaron {datos_producto['Cantidad']} unidades")

        inventario.append(datos_producto)
        opcion3 = int(input('''presione 1 para seguir cargando
presione 2 para volver: '''))
        
        if not inventario:
                print("No se tienen productos cargados")
                break
            
        else:
            print("Se tiene el siguiente inventario.")
            print ("PRODUCTO                    PRECIO")
            for producto in inventario:
                print(f"{producto['Producto']}                            {producto['Precio']}$")

        if (opcion3 <1) or (opcion3 > 2):
            print('ingrese un valor valido') 
        
        elif opcion3 == 2: 
            print("Decidió salir del sistema de cargado.")

    elif opcion == 2:
#En esta seccion el usuario podrá comprar productos

        print("Sistema de clientes.")

        while True:
            print("Marque 1 para ver el inventario")
            print("Marque 2 para comprar")
            opcion2 = int(input("""
Indique la opción a tomar:  """))

            if opcion2 == 1:
                if not inventario:
                    print("No hay productos en stock.")
                else:
                    print("PRODUCTO                    PRECIO")
                    for producto in inventario:
                        print(f"{producto['Producto']}                            {producto['Precio']}$")

            elif opcion2 == 2:
                print("Va a comprar")
                for i in range(len(inventario)):
                    producto = inventario[i]
                    print(f"Marque {i + 1} si desea comprar {producto['Producto']}")

                compra = int(input("Indique el número de compra: "))
                if compra < 1 or compra > len(inventario):
                    print("El número de compra es inválido.")
                else:
                #Debe restarse uno a la seccion del interes en el inventario ya que asi me dará el producto que se tomó realmente
                    producto_seleccionado = inventario[compra - 1]

                    if producto_seleccionado['Cantidad'] > 0:
                        cantidad = int(input(f"¿Cuántas cantidades desea de {producto_seleccionado['Producto']}?: "))
                        if cantidad > producto_seleccionado['Cantidad']:
                            print("No hay suficiente stock para la compra de este artículo.")
                        else:
                            precio_total = cantidad * producto_seleccionado['Precio']
                            producto_seleccionado['Cantidad'] -= cantidad
#Hacemos un diccionario de los datos del producto, cantidad y precio de los articulos
                            producto_carrito = {
                                'Producto': producto_seleccionado['Producto'],
                                'Cantidad': cantidad,
                                'Precio': producto_seleccionado['Precio'],
                            }

                            carrito.append(producto_carrito)
# Se calcula el precio total de la compra
                            print(f"Ha comprado {cantidad} unidades de {producto_seleccionado['Producto']} por {precio_total}$.")

                            opcion5 = input("""¿Desea seguir comprando?
Marque 1 para sí
Marque 2 para no: """)
                            if opcion5 == "2":
                                print("Factura de compra:")
                                print("Producto                    Cantidad      Precio")
                                print("-----------------------------------------------")
                                for producto in carrito:
                                    print(f"{producto['Producto']}        {producto['Cantidad']}               {producto['Precio']}$")
                                print("-----------------------------------------------")
#Rea lizamos la sumatoria de la compra con un ciclo for, dentro de la misma variable 
                                total_pagar = sum(producto['Precio'] * producto['Cantidad'] for producto in carrito)
                                
                                print(f"Total a pagar: {total_pagar}$")
                                print("Gracias por utilizar nuestro sistema de compras.")
                                opcion = 0  # Reiniciamos el bucle principal otra vez
                                break
                            
                            elif opcion5 != "1" and opcion5 != "2":
                                print("Comando no válido.")
                    else:
                        print(f"No hay suficiente cantidad de {producto_seleccionado['Producto']} en el inventario.")

                if compra > len(inventario):
                    raise ValueError("No se puede comprar productos con este código ya que no existen.")
                break

            else:
                print("Ingrese una opción válida.")

    else:
        print("Ingrese una opción válida.")

    print("\n-----------------------------------------------------------\n")

    while True:
        print("""Marque 1 si es empleado
Marque 2 si es cliente
Marque 0 para salir: """)
        opcion = int(input("Ingrese su opción: "))

        if opcion == 1 or opcion == 2 or opcion == 0:
            break
        else:
            print("Ingrese una opción válida.")

print("Gracias por utilizar nuestro sistema. ¡Hasta pronto!")

if opcion == 3:
    print("Gracias por utilizar el sistema.")