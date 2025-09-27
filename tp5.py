import random

# 1) 
notas = [random.randint(1, 10) for _ in range(10)]
print("Notas de los estudiantes:")
for nota in notas:
    print(nota)
print("Promedio:", sum(notas) / len(notas))
print("Nota mas alta:", max(notas))
print("Nota ms baja:", min(notas))

# 2) 
productos = []
for _ in range(5):
    productos.append(input("Ingresa un producto: "))
print("Lista ordenada:", sorted(productos))
eliminar = input("Que producto queres eliminar?: ")
if eliminar in productos:
    productos.remove(eliminar)
print("Lista actualizada:", productos)

# 3) 
numeros = [random.randint(1, 100) for _ in range(15)]
pares = []
impares = []
for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print("Cantidad de pares:", len(pares))
print("Cantidad de impares:", len(impares))

# 4) 
lista = [1, 2, 2, 3, 4, 4, 5, 1, 6]
sin_repetidos = []
for elem in lista:
    if elem not in sin_repetidos:
        sin_repetidos.append(elem)
print("Lista sin repetidos:", sin_repetidos)

# 5)
estudiantes = ["Ana", "Luis", "Pedro", "Sofía", "Juan", "Lucía", "Carlos", "María"]
accion = input("queresd agregar (A) o eliminar (E) un estudiante?: ").upper()
if accion == "A":
    nuevo = input("Ingresa el nombre del nuevo estudiante: ")
    estudiantes.append(nuevo)
elif accion == "E":
    eliminar = input("Ingresa el nombre del estudiante a eliminar: ")
    if eliminar in estudiantes:
        estudiantes.remove(eliminar)
print("Lista final:", estudiantes)

# 6)
numeros = [random.randint(1, 100) for _ in range(7)]
print("Lista original:", numeros)
rotada = [numeros[-1]] + numeros[:-1]
print("Lista rotada:", rotada)

# 7)
temperaturas = [[random.randint(0, 15), random.randint(16, 35)] for _ in range(7)]
minimas = [dia[0] for dia in temperaturas]
maximas = [dia[1] for dia in temperaturas]
print("Temperaturas (mínima, máxima) por día:")
for dia in temperaturas:
    print(dia)
print("Promedio mínimas:", sum(minimas) / 7)
print("Promedio máximas:", sum(maximas) / 7)
amplitudes = [maximas[i] - minimas[i] for i in range(7)]
print("Mayor amplitud térmica en el día:", amplitudes.index(max(amplitudes)) + 1)

# 8)
notas = [[random.randint(1, 10) for _ in range(3)] for _ in range(5)]
print("Notas por estudiante:")
for fila in notas:
    print(fila)
for i, fila in enumerate(notas):
    print(f"Promedio estudiante {i+1}:", sum(fila) / 3)
for j in range(3):
    suma = 0
    for i in range(5):
        suma += notas[i][j]
    print(f"Promedio materia {j+1}:", suma / 5)

# 9) 
tablero = [["-" for _ in range(3)] for _ in range(3)]
def mostrar_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))
for turno in range(9):
    jugador = "X" if turno % 2 == 0 else "O"
    print(f"Turno de {jugador}")
    fila = int(input("Fila (0-2): "))
    col = int(input("Columna (0-2): "))
    if tablero[fila][col] == "-":
        tablero[fila][col] = jugador
    mostrar_tablero(tablero)

# 10) 
ventas = [[random.randint(0, 20) for _ in range(7)] for _ in range(4)]
print("Ventas por producto y día:")
for fila in ventas:
    print(fila)
for i, fila in enumerate(ventas):
    print(f"Total producto {i+1}:", sum(fila))
totales_dia = [sum(ventas[j][i] for j in range(4)) for i in range(7)]
print("Día con mayores ventas:", totales_dia.index(max(totales_dia)) + 1)
totales_producto = [sum(fila) for fila in ventas]
print("Producto más vendido:", totales_producto.index(max(totales_producto)) + 1)