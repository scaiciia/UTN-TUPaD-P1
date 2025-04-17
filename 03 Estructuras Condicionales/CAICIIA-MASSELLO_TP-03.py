# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
#     deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad = int(input("Ingrese una edad: "))

if (edad > 18):
    print("Es mayor de edad")


# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, 
# deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar
# el mensaje “Desaprobado”.

nota = int(input("Ingrese una nota: "))

if (nota >= 6):
    print("Aprobado")
else:
    print("Desaprobado")


# 3) Escribir un programa que permita ingresar solo números pares. 
# Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un 
# número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". 
# Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es 
# par o impar.

num = int(input("Ingrese un numero: "))

if (num % 2 == 0):
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")


# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla
#   a cuál de las siguientes categorías pertenece:
#       ● Niño/a: menor de 12 años.
#       ● Adolescente: mayor o igual que 12 años y menor que 18 años.
#       ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#       ● Adulto/a: mayor o igual que 30 años.

edad = int(input("Ingrese una edad: "))

if (edad < 12):
    print("Niño/a")
elif ((edad >= 12) and (edad < 18)):
    print("Adolescente")
elif ((edad > 18) and (edad < 30)):
    print("Adulto/a joven")
else:
    print("Adulto/a")


# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres 
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir
# en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir 
# por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: 
# investigue el uso de la función len() en Python para evaluar la cantidad de elementos que 
# tiene un iterable tal como una lista o un string.

password = input("Ingrese una contraseña: ")

long = len(password)
if ((long >= 8) and (long <= 14)):
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


# 6) El paquete statistics de python contiene funciones que permiten tomar una lista de números
# y calcular la moda, la mediana y la media de dichos números.
# En la documentación oficial se puede encontrar más información sobre este paquete: 
# https://docs.python.org/es/3.8/library/statistics.html.
# La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se 
# pueden utilizar para predecir la forma de una distribución normal a partir del siguiente 
# criterio:
#     ● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la mediana es mayor que la moda.
#     ● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, la mediana es menor que la moda.
#     ● Sin sesgo: cuando la media, la mediana y la moda son iguales.
# Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista 
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si 
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
# Definir la lista numeros_aleatorios de la siguiente forma:
# Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de 
# forma aleatoria.

from statistics import mode, median, mean
import random

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

if ((media > mediana) and (mediana > moda)):
    print("Sesgo positivo o a la derecha")
elif ((media < mediana) and (mediana < moda)):
    print("Sesgo negativo o a la izquierda")
elif ((media == mediana) and (mediana == moda)):
    print("Sin sesgo")


# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de 
# exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el 
# usuario e imprimirlo por pantalla.

frase = input("Ingrese una palabra o frase: ")

letra = frase[-1].lower()

if letra in "aeiou":
    frase += "!"

print(frase)


# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por 
# pantalla. Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir entre mayúsculas y minúsculas.

print("1. Si quiere su nombre en MAYÚSCULAS")
print("2. Si quiere su nombre en minúsculas")
print("3. Si quiere su nombre con la primera letra Mayúscula")
nombre = input("Ingrese su nombre: ")
numero = int(input("Ingrese un numero: "))
resultado = ""

if (numero == 1):
    resultado = nombre.upper()
elif (numero == 2):
    resultado = nombre.lower()
elif (numero == 3):
    resultado = nombre.capitalize()

print("Resultado: ", resultado)


# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías 
# según la escala de Richter e imprima el resultado por pantalla:
#     ● Menor que 3: "Muy leve" (imperceptible).
#     ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#     ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
#     ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
#     ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#     ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

valor = int(input("Ingrese el valor del terremoto en escala Ritcher: "))
resultado = ""

if (valor < 3):
    resultado = "Muy leve"
elif ((valor >= 3) and (valor < 4)):
    resultado = "Leve"
elif ((valor >= 4) and (valor < 5)):
    resultado = "Moderado"
elif ((valor >= 5) and (valor < 6)):
    resultado = "Fuerte"
elif ((valor >= 6) and (valor < 7)):
    resultado = "Muy fuerte"
else:
    resultado = "Extremo"

print("Resultado: ", resultado)


# 10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año 
# Periodo del año     Estación en el hemisferio norte        Estación en el hemisferio sur

# Desde el 21 de 
# diciembre hasta     Invierno                               Verano
# el 20 de marzo 
# (incluidos)

# Desde el 21 de 
# marzo hasta el      Primavera                              Otoño
# 20 de junio
# (incluidos)

# Desde el 21 de
# junio hasta el      Verano                                 Invierno
# 20 de septiembre 
# (incluidos)

# Desde el 21 de 
# septiembre hasta    Otoño                                  Primavera
# el 20 de diciembre 
# (incluidos)

# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del 
# año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el 
# usuario se encuentra en otoño, invierno, primavera o verano.

from datetime import datetime

hemisferio = input("En que hemisferio te encuentras? (N/S): ").strip().upper()
mes = int(input("Ingrese el mes (1-12): "))
dia = int(input("Ingrese el dia (1-31): "))

fecha = datetime(2025, mes, dia)

if ((datetime(2025, 12, 21) <= fecha) or (datetime(2025, 3, 20) >= fecha)):
    if (hemisferio == "N"):
        estacion = "Invierno"
    else:
        estacion = "Verano"
elif ((datetime(2025, 3, 21) <= fecha) or (datetime(2025, 6, 20) >= fecha)):
    if (hemisferio == "N"):
        estacion = "Primavera"
    else:
        estacion = "Otoño"
elif ((datetime(2025, 6, 21) <= fecha) or (datetime(2025, 9, 20) >= fecha)):
    if (hemisferio == "N"):
        estacion = "Verano"
    else:
        estacion = "Invierno"
else:
    if (hemisferio == "N"):
        estacion = "Otoño"
    else:
        estacion = "Primavera"
    
print(f"Estas en {estacion}")