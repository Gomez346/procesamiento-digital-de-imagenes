numeros = []

for i in range(7):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    numeros.append(numero)


contador = {}

for numero in numeros:
    if numero in contador:
        contador[numero] += 1
    else:
        contador[numero] = 1


numero_mas_repetido = None
max_repeticiones = 0

for numero, repeticiones in contador.items():
    if repeticiones > max_repeticiones:
        numero_mas_repetido = numero
        max_repeticiones = repeticiones


print(f"El número que más se repite es {numero_mas_repetido} y se repite {max_repeticiones} veces.")
