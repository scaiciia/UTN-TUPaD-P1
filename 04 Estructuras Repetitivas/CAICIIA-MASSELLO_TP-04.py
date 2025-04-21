# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(101):
    print(i)


# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

numero = int(input("Ingrese un número entero: "))

c = 0
while numero > 0:
    numero //= 10
    c += 1

print("La cantidad de dígitos es: ", c)


# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

suma = 0
for i in range(num1 + 1, num2):
    suma += i

print("La suma de los números enteros entre", num1, "y", num2, "es:", suma)


# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

suma = 0

while True:
    num = int(input("Ingrese un número entero (0 para salir): "))
    if num == 0:
        break
    suma += num

print("La suma total es:", suma)


# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random

c = 0
num = random.randint(0, 9)
adivinado = False

while not adivinado:
    c += 1
    intento = int(input("Adivina el número entre 0 y 9: "))
    if intento == num:
        adivinado = True
    else:
        print("Intenta de nuevo.")

print("Adivinaste el número en ", c, " intentos.")


# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

for i in range(98, 0, -2):
    print(i)


# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

num = int(input("Ingrese un número entero positivo: "))
while num < 0:
    num = int(input("Por favor, ingrese un número entero positivo: "))

suma = 0
for i in range(num):
    suma += i

print("La suma de los números enteros desde 0 hasta", num, " es: ", suma)


# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

pares = 0
impares = 0
negativos = 0
positivos = 0

for i in range(100):
    num = int(input("Ingrese un número entero: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

    if num < 0:
        negativos += 1
    elif num > 0:
        positivos += 1

print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)
print("Cantidad de números negativos:", negativos)
print("Cantidad de números positivos:", positivos)


# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

total = 100
suma = 0

for i in range(total):
    num = int(input("Ingrese un número entero: "))
    suma += num

media = suma / total
print("La media de los números ingresados es:", media)


# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

num = int(input("Ingrese un número entero: "))
invertido = 0

while num > 0:
    invertido = invertido * 10 + num % 10
    num //= 10

print("El número invertido es:", invertido)