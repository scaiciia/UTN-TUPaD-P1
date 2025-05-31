# -*- coding: utf-8 -*-
# Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.

def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()


# Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y 
# devuelva un saludo personalizado. Por ejemplo, si se llama con saludar_usuario("Marcos"),  
# deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando 
# el nombre al usuario.

def saludar_usuario(nombre):
    return f"Hola {nombre}!"

nombre = input("Ingrese su nombre: ")
print(saludar_usuario(nombre))


# Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba
# cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
# Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su lugar de residencia: ")
informacion_personal(nombre, apellido, edad, residencia)


# Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva 
# el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y 
# devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para 
# mostrar los resultados.

import math

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

radio = float(input("Ingrese el radio del círculo: "))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)
print(f"Un círculo de radio {radio} tiene un área de {area:.2f} y un perímetro de {perimetro:.2f}.")


# Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como 
# parámetro y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos 
# y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    return segundos / 3600

segundos = int(input("Ingrese la cantidad de segundos: "))
horas = segundos_a_horas(segundos)
print(f"{segundos} segundos son {horas:.2f} horas")

# Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y 
# imprima la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar 
# a la función

def tabla_multiplicar(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} * {i} = {resultado}")

numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
tabla_multiplicar(numero)


# Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y 
# devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. 
# Mostrar los resultados de forma clara.

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b != 0:
        division = a / b
    else:
        division = "Error: División por cero"
    
    return (suma, resta, multiplicacion, division)

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
resultados = operaciones_basicas(a, b)
print(f"{a} + {b} = {resultados[0]}\n{a} - {b} = {resultados[1]}\n{a} * {b} = {resultados[2]}\n{a} / {b} = {resultados[3]}")


# Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la 
# altura en metros, y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y 
# llamar a la función para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
imc = calcular_imc(peso, altura)
print(f"Su IMC es {imc:.2f}")


# Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados 
# Celsius y devuelva su equivalente en Fahrenheit. Pedir al usuario la temperatura en Celsius y 
# mostrar el resultado usando la función.

def celsius_a_fahrenheit(celsius):
    fahrenheit = 9/5 * celsius + 32
    return fahrenheit

celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"{celsius}˚C son {fahrenheit:.2f}˚F")


# Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y 
# devuelva el promedio de ellos. Solicitar los números al usuario y mostrar el resultado usando 
# esta función.

def calcular_promedio(a, b, c):
    suma = a + b + c
    promedio = suma / 3
    return promedio

a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))

promedio = calcular_promedio(a, b, c)
print(f"El promedio de {a}, {b} y {c} es {promedio:.2f}")