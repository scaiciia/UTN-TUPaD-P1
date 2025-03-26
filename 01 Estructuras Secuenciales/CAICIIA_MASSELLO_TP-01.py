# P1E1
print('Hola Mundo!')

# P1E2
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

# P1E3
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# P1E4
import math

radio = float(input("Ingrese el radio del círculo: "))
perimetro = 2 * math.pi * radio
area = math.pi * radio ** 2
print(f"Un circulo de radio {radio} tiene un perímetro de {perimetro} y un área de {area}.")

# P1E5
segundos = int(input("Ingrese la cantidad de segundos: "))
horas = segundos / 3600
print(f"{segundos} segundos son {horas} horas")

# P1E6
n = int(input("Ingrese un numero: "));
resultado = n * 1;
print(f"{n} * 1 = {resultado}");
resultado = n * 2;
print(f"{n} * 2 = {resultado}");
resultado = n * 3;
print(f"{n} * 3 = {resultado}");
resultado = n * 4;
print(f"{n} * 4 = {resultado}");
resultado = n * 5;
print(f"{n} * 5 = {resultado}");
resultado = n * 6;
print(f"{n} * 6 = {resultado}");
resultado = n * 7;
print(f"{n} * 7 = {resultado}");
resultado = n * 8;
print(f"{n} * 8 = {resultado}");
resultado = n * 9;
print(f"{n} * 9 = {resultado}");
resultado = n * 10;
print(f"{n} * 10 = {resultado}");

# P1E7
n1 = int(input("Ingrese un numero distinto de 0: "));
n2 = int(input("Ingrese otro numero distinto de 0: "));
resultado = n1 + n2;
print(f"{n1} + {n2} = {resultado}");
resultado = n1 - n2;
print(f"{n1} - {n2} = {resultado}");
resultado = n1 * n2;
print(f"{n1} * {n2} = {resultado}");
resultado = n1 / n2;
print(f"{n1} / {n2} = {resultado}");

# P1E8
altura = float(input("Ingrese su altura: "));
peso = float(input("Ingrese su peso: "));
imc = peso / (altura ** 2);
print(f"Su IMC es {imc}");

# P1E9
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = 9/5 * celsius + 32;
print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit");

# P1E10
n1 = int(input("Ingrese el primer numero: "));
n2 = int(input("Ingrese el segundo numero: "));
n3 = int(input("Ingrese el tercer numero: "));
suma = n1 + n2 + n3;
promedio = suma / 3;
print(f"El promedio de {n1}, {n2} y {n3} es {promedio}");