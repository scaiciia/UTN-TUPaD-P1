# Dado el diccionario precios_frutas

# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# Añadir las siguientes frutas con sus respectivos precios:
#     ● Naranja = 1200
#     ● Manzana = 1500
#     ● Pera = 2300

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)


# Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
#     ● Banana = 1330
#     ● Manzana = 1700
#     ● Melón = 2800

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)


# Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas 
# sin los precios.

lista_frutas = list(precios_frutas.keys())

print(lista_frutas)

# Escribí un programa que permita almacenar y consultar números telefónicos.
#     • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
#     • Luego, pedí un nombre y mostrale el número asociado, si existe.

contactos = {}

for i in range(5):
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el número de teléfono: ")
    contactos[nombre] = numero

nombre_consulta = input("Ingrese el nombre del contacto a consultar: ")
if nombre_consulta in contactos:
    print(f"El número de teléfono de {nombre_consulta} es: {contactos[nombre_consulta]}")
else:
    print(f"No se encontró el contacto: {nombre_consulta}")


# Solicita al usuario una frase e imprime:
#     • Las palabras únicas (usando un set).
#     • Un diccionario con la cantidad de veces que aparece cada palabra.

frase = input("Ingrese una frase: ")
palabras = frase.split()

palabras_unicas = set(palabras)
print("Palabras únicas:", palabras_unicas)

conteo_palabras = {}
for palabra in palabras:
    if palabra in conteo_palabras:
        conteo_palabras[palabra] += 1
    else:
        conteo_palabras[palabra] = 1
print("Cantidad de veces que aparece cada palabra:", conteo_palabras)


# Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 
# 3 notas. Luego, mostrá el promedio de cada alumno.

alumnos = {}

for i in range(3):
    nombre = input("Ingrese el nombre del alumno: ")
    notas = input("Ingrese las 3 notas separadas por comas: ")
    notas_tupla = tuple(map(float, notas.split(',')))
    alumnos[nombre] = notas_tupla

for alumno, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {alumno} es: {promedio:.2f}")


# Dado dos sets de números, representando dos listas de estudiantes que 
# aprobaron Parcial 1 y Parcial 2:
#     • Mostrá los que aprobaron ambos parciales.
#     • Mostrá los que aprobaron solo uno de los dos.
#     • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

parcial1 = {101071, 100529, 100389, 101382, 101211}
parcial2 = {101071, 100529, 100278, 101382}

aprobados_ambos = parcial1.intersection(parcial2)
print("Aprobados en ambos parciales:", aprobados_ambos)

aprobados_uno = parcial1.symmetric_difference(parcial2)
print("Aprobados solo en uno de los dos:", aprobados_uno)

aprobados_total = parcial1.union(parcial2)
print("Lista total de estudiantes que aprobaron al menos un parcial:", aprobados_total)


# Armá un diccionario donde las claves sean nombres de productos y los 
# valores su stock. Permití al usuario:
#     • Consultar el stock de un producto ingresado.
#     • Agregar unidades al stock si el producto ya existe.
#     • Agregar un nuevo producto si no existe.

productos = {"shampoo": 50, "jabón": 30, "detergente": 20}

def consultar_stock(producto):
    return productos.get(producto, "Producto no encontrado.")

def agregar_stock(producto, unidades):
    if producto in productos:
        productos[producto] += unidades
        return f"Stock actualizado. Nuevo stock de {producto}: {productos[producto]}"
    else:
        productos[producto] = unidades
        return f"Producto {producto} agregado con stock inicial de {unidades}."
    
while True:
    accion = int(input("Ingrese '1' para consultar stock, '2' para agregar stock o '3' para terminar: "))
    
    if accion == 1:
        producto = input("Ingrese el nombre del producto a consultar: ").strip().lower()
        print(consultar_stock(producto))
    elif accion == 2:
        producto = input("Ingrese el nombre del producto a agregar: ").strip().lower()
        unidades = int(input("Ingrese la cantidad de unidades a agregar: "))
        print(agregar_stock(producto, unidades))
    elif accion == 3:
        print("Terminando el programa.")
        break
    else:
        print("Acción no reconocida. Intente nuevamente.")


# Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Permití consultar qué actividad hay en cierto día y hora.

agenda = {
    ('lunes', '10:00'): 'Reunión',
    ('martes', '15:00'): 'Clase de inglés'
}

def agregar_evento(dia, hora, evento):
    agenda[(dia, hora)] = evento
    print(f"Evento '{evento}' agregado para {dia} a las {hora}.")

def consultar_evento(dia, hora):
    fecha_hora = (dia, hora)
    if fecha_hora in agenda:
        print(f"Evento en {dia} a las {hora}: {agenda[fecha_hora]}")
    else:
        print(f"No hay eventos programados para {dia} a las {hora}.")

while True:
    accion = int(input("Ingrese '1' para agregar un evento, '2' para consultar un evento o '3' para salir: "))
    
    if accion == 1:
        dia = input("Ingrese el día del evento (ejemplo: Lunes): ")
        hora = input("Ingrese la hora del evento (ejemplo: 10:00): ")
        evento = input("Ingrese el nombre del evento: ")
        agregar_evento(dia, hora, evento)
    elif accion == 2:
        dia = input("Ingrese el día a consultar (ejemplo: Lunes): ")
        hora = input("Ingrese la hora a consultar (ejemplo: 10:00): ")
        consultar_evento(dia, hora)
    elif accion == 3:
        print("Saliendo de la agenda.")
        break
    else:
        print("Acción no reconocida. Intente nuevamente.")


# Dado un diccionario que mapea nombres de países con sus capitales, construí un 
# nuevo diccionario donde:
#     • Las capitales sean las claves.
#     • Los países sean los valores.

original = {
    'Argentina': 'Buenos Aires',
    'Brasil': 'Brasilia',
    'Chile': 'Santiago',
    'Colombia': 'Bogotá',
    'Perú': 'Lima'
}
invertido = {}

for pais, capital in original.items():
    invertido[capital] = pais

print(f"original: {original}")
print(f"invertido: {invertido}")