# 1) 
edad = int(input("Ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad")

# 2) 
nota = int(input("Ingresa su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado, perri")

# 3) 
numero = int(input("Ingresa un numero par: "))
if numero % 2 == 0:
    print("Ha ingresado un numero par")
else:
    print("Por favor, ingresa un numero par")

# 4) 
edad = int(input("Ingresa tu edad: "))
if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

# 5) 
contraseña = input("Ingresa una contraseña: ")
if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# 6) 

import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

print("Moda:", moda)
print("Mediana:", mediana)
print("Media:", media)


if media > mediana and mediana > moda:
    print("Sesgo positivo o a la derecha")
elif media < mediana and mediana < moda:
    print("Sesgo negativo o a la izquierda")
elif media == mediana and mediana == moda:
    print("Sin sesgo")
else:
    print("No se puede determinar el sesgo con claridad")

# 7) 
frase = input("Ingresa una frase o palabra: ")
if frase[-1].lower() in "aeiou":
    print(frase + "!")
else:
    print(frase)

# 8) 
nombre = input("Ingresa su nombre: ")
opcion = input("Ingresa 1 para mayusculas, 2 para minusculas, 3 para primera letra mayuscula: ")

if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())
else:
    print("Opcion invalida")

# 9)
magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras debiles)")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")

# 10)
hemisferio = input("¿En qué hemisferio se encuentra? (N/S): ").upper()
mes = int(input("Ingrese el mes (1-12): "))
dia = int(input("Ingrese el día (1-31): "))

# Convertir la fecha a un numero para facilitar la comparación
fecha = mes * 100 + dia

if 1221 <= fecha <= 1231 or 101 <= fecha <= 320:
    # 21 dic - 31 diciembre o 1 ene - 20 mar
    if hemisferio == "N":
        estacion = "Invierno"
    else:
        estacion = "Verano"
elif 321 <= fecha <= 620:
    # 21 mar - 20 jun
    if hemisferio == "N":
        estacion = "Primavera"
    else:
        estacion = "Otoño"
elif 621 <= fecha <= 920:
    # 21 jun - 20 sep
    if hemisferio == "N":
        estacion = "Verano"
    else:
        estacion = "Invierno"
elif 921 <= fecha <= 1220:
    # 21 sep - 20 dic
    if hemisferio == "N":
        estacion = "Otono"
    else:
        estacion = "Primavera"
else:
    estacion = "Fecha inválida"

print("Estación:", estacion)

