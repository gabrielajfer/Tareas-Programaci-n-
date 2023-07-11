##EJERCICIO 2 EL CARACOL

h_pozo = int(input("Ingrese la profundidad del pozo en metros: "))
subida_dia = int(input("Ingrese la distancia que asciende el caracol durante el día en metros: "))
caida_noche = int(input("Ingrese la distancia que cae el caracol en la noche en metros: "))

if caida_noche > subida_dia:
    print("El Caracol nunca saldrá si es mas lo que cae que lo que sube.")

else:
  posicion = 0
  tiempo = 0
  #Hago un ciclo para el recorrido del caracol

  while subida_dia < h_pozo:

    tiempo += 24
    posicion += (subida_dia - caida_noche)
    if posicion >= h_pozo:
     tiempo_en_dias = tiempo //24
     print(f"el caracol sale en: {tiempo_en_dias} dias.")
     break