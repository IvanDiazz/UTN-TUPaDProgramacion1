# 1) Imprimir numeros del 0 al 100
for i in range(101):
    print(i)

# 2) Cantidad de dígitos de un numero
num = int(input("Ingresa un numero entero: "))
print("Cantidad de dígitos:", len(str(abs(num))))

# 3) Suma de numeros entre dos valores (excluyendo extremos)
a = int(input("Ingresa el primer valor: "))
b = int(input("Ingresa el segundo valor: "))
print("Suma:", sum(range(min(a, b) + 1, max(a, b))))

# 4) Sumar numeros hasta ingresar 0
total = 0
while True:
    n = int(input("Ingresa un numero (0 para terminar): "))
    if n == 0:
        break
    total += n
print("Total acumulado:", total)

# 5) Juego de adivinanza
import random
objetivo = random.randint(0, 9)
intentos = 0
while True:
    intento = int(input("Adivina el numero (0-9): "))
    intentos += 1
    if intento == objetivo:
        print("¡Correcto! Intentos:", intentos)
        break

# 6) Números pares de 100 a 0 en orden decreciente
for i in range(100, -1, -2):
    print(i)

# 7) Suma de números entre 0 y un valor dado
n = int(input("Ingresa un numero entero positivo: "))
print("Suma:", sum(range(n + 1)))

# 8) Contar pares, impares, negativos y positivos en 100 números
pares = impares = negativos = positivos = 0
for _ in range(100):  # Cambia 100 por otro valor para probar
    num = int(input("Ingresa un numero: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num < 0:
        negativos += 1
    elif num > 0:
        positivos += 1
print("Pares:", pares)
print("Impares:", impares)
print("Negativos:", negativos)
print("Positivos:", positivos)

# 9) Media de 100 números ingresados
suma = 0
for _ in range(100):  # Cambia 100 por otro valor para probar
    num = int(input("Ingresa un numero: "))
    suma += num
print("Media:", suma / 100)

# 10) Invertir los dígitos de un numero
num = input("Ingresa un numero: ")
print("NNumero invertido:", num[::-1])