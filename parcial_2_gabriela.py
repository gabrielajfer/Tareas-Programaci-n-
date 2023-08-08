import json

# Función para guardar datos en un archivo JSON
def save_from_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Función para leer un archivo JSON en Python
def read_from_json(file_path):
    data = None
    
    try:
        with open(file_path) as file:
            data = json.load(file)
    except FileNotFoundError:
        pass
        
    return data

# Función para crear un archivo JSON vacío
def create_json(file_path):
    data = []
    with open(file_path, 'w') as file:
        json.dump(data, file)

# Función para agregar un alumno y sus detalles
def agregar_estudiantes(data):

  nombre = input("Ingrese nombre y apellido: ")
  edad = int(input("Ingrese edad del estudiante: "))
  
  notas = ingresar_notas()
  
  alumno = {
    "Nombre": nombre, 
    "Edad": edad,
    "Notas": notas
  }

  data.append(alumno)

def ingresar_notas():
  notas = []
  nota = input("Ingrese nota (1-10, 'x' para finalizar): ")

  while nota != 'x':
    if validar_nota(nota):
      notas.append(float(nota))
    else:
      print("Nota inválida. Intente de nuevo (1-10)")

    nota = input("Ingrese otra nota ('x' para finalizar): ")

  return notas

def validar_nota(nota):
  if nota.isdigit() and 1 <= int(nota) <= 10:
    return True

  return False

# Función para listar todos los alumnos y sus notas
def listar_estudiantes(data):

  for alumno in data:
      
    print(alumno["Nombre"])
    print(alumno["Edad"])
    
    for nota in alumno["Notas"]:
      print(nota, end=" ")
    
    print("\n" + "-"*10)
    
# Función para calcular el promedio de notas de la clase
def calcular_promedio(data):

  notas = []

  for alumno in data:
    
    nombre = alumno["Nombre"]
    print(f"Procesando alumno: {nombre}")
    
    edad = alumno["Edad"]
    print(f"Edad: {edad}")

    evaluaciones = alumno["Notas"]
    print(f"Cantidad de evaluaciones: {len(evaluaciones)}")

    print("Notas:")
    for nota in evaluaciones:
      print(nota)
      notas.append(nota)

  print(f"Total notas: {len(notas)}")

  suma = 0
  for nota in notas:
    suma = suma + nota
    print(f"Sumando nota...Suma actual: {suma}")

  promedio = suma / len(notas)
  print(f"Promedio calculado: {promedio}")

  return promedio

# Función para encontrar la nota máxima y mínima
def encontar_max_min(data):
    max_nota = 10
    min_nota = 0
    alumno_max = ""
    alumno_min = ""
    
    for alumno in data:
        for nota in alumno['Notas']:
            if nota > max_nota:
                max_nota = nota
                alumno_max = alumno['Nombre']
            if nota < min_nota:
                min_nota = nota
                alumno_min = alumno['Nombre']
    
    return max_nota, alumno_max, min_nota, alumno_min

# Función que muestra el menú principal y maneja la interacción con el usuario
def menu_principal(data):
    while True:
        mostrar_menu()

        opcion = input("Seleccione una opción (1-6): ")
        
        if opcion == "1":
            agregar_estudiantes(data)
        elif opcion == "2":
            listar_estudiantes(data)
        elif opcion == "3":
            promedio = calcular_promedio(data)
            print(f"Promedio de Notas de la Clase: {promedio:.2f}")
        elif opcion == "4":
            max_nota, alumno_max, min_nota, alumno_min = encontar_max_min(data)
            print(f"Nota Máxima: {max_nota} (Alumno: {alumno_max})")
            print(f"Nota Mínima: {min_nota} (Alumno: {alumno_min})")
        elif opcion == "5":
            save_from_json(data, sistema_notasucv_json)
            print("Datos guardados correctamente.")
        elif opcion == "6":
            print("Saliendo del programa.")
            break
        else:
            print("No es una opción válida. Seleccione un número del 1 al 6.")

# Función que muestra el menú al usuario
def mostrar_menu():
    print("Bienvenido al Sistema de Notas UCV")
    print("Por favor ingrese su opción:")
    print("Marque 1 para ingresar un nuevo alumno")
    print("Marque 2 para listarlos")
    print("Marque 3 para calcular el promedio de la clase")
    print("Marque 4 para saber nota maxima y minima")
    print("Marque 5 para guardar los datos")
    print("Marque 6 si terminó su trabajo")

# Nombre del archivo JSON
sistema_notasucv_json = "sistemaucv.json"

data = read_from_json(sistema_notasucv_json)

if data is None:
    create_json(sistema_notasucv_json)
    data = []

# Se llama la funcion
menu_principal(data)