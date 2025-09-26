# 1)

print (f"Hola mundo!")


# 2)
nombre = input("Escriba su nombre: ")

print (f"Hola! " + nombre)

# 3)

nombre = input ("Escriba su nombre ")

apellido = input ("Escriba su apellido ")

edad = input ("Escriba su edad ")

residencia = input ("Escriba su lugar de residencia ")


print(f"Hola me llamo " + nombre + " mi apellido es " + apellido + ", tengo " + edad + " años y vivo en " + residencia + "." )

# 4)

radio = float(input("Escriba el radio del circulo: "))

area = 3.14 * radio * radio
perimetro = 2 * 3.14 * radio

print(f"El área del círculo es: {area}")
print(f"El perímetro del círculo es: {perimetro}")

# 5)

segundos = int(input("Escriba cuantos segundos: "))

horas = segundos / 3600

print("Eso equivale a", horas, "horas")

# 6)

numero = int(input("Escriba un numero: "))

print("Tabla de multiplicar del", numero)

print(numero, "x 1 =", numero * 1)
print(numero, "x 2 =", numero * 2)
print(numero, "x 3 =", numero * 3)
print(numero, "x 4 =", numero * 4)
print(numero, "x 5 =", numero * 5)
print(numero, "x 6 =", numero * 6)
print(numero, "x 7 =", numero * 7)
print(numero, "x 8 =", numero * 8)
print(numero, "x 9 =", numero * 9)
print(numero, "x 10 =", numero * 10)


# 7)

numero1 = int(input("Escribqa el primer numero (distinto de 0): "))
numero2 = int(input("Escriba el segundo numero (distinto de 0): "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

print("La suma es:", suma)
print("La resta es:", resta)
print("La multiplicación es:", multiplicacion)
print("La división es:", division)
