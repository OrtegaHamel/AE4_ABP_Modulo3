# Ejercicio 1: Básico
# Imprime todos los números enteros del 0 al 100
print("Ejercicio 1: Números del 0 al 100")
for i in range(101):
    print(i)

# Ejercicio 2: Múltiplos de 2 entre 2 y 500
print("Ejercicio 2: Múltiplos de 2 del 2 al 500")
for i in range(2, 501, 2):
    print(i)

# Ejercicio 3: Contando Vanilla Ice
# Imprime del 1 al 100, reemplazando múltiplos de 5 por "ice ice" y múltiplos de 10 por "baby"
print("Ejercicio 3: Contando Vanilla Ice")
for i in range(1, 101):
    if i % 10 == 0:
        print("baby")
    elif i % 5 == 0:
        print("ice ice")
    else:
        print(i)   

# Ejercicio 4: Wow. Número gigante a la vista
# Suma los números pares del 0 al 500000
print("Ejercicio 4: Sumando números pares del 0 al 500000")
suma_pares = 0
for i in range(0, 500001, 2):
    suma_pares += i
print(f"Suma total de pares: {suma_pares}")

# Ejercicio 5: Regrésame al 3
# Cuenta regresiva desde 2024 de 3 en 3
print("Ejercicio 5: Cuenta regresiva desde 2024 de 3 en 3")
for i in range(2024, 0, -3):
    print(i)

# Ejercicio 6: Contador dinámico
# Imprime múltiplos de 'multiplo' entre num_inicial y num_final
print("Ejercicio 6: Contador dinámico")

num_inicial = int(input("Ingrese el número inicial: "))
num_final = int(input("Ingrese el número final: "))
multiplo = int(input("Ingrese el número múltiplo: "))

print(f"Números entre {num_inicial} y {num_final} que son múltiplos de {multiplo}:")
for i in range(num_inicial, num_final + 1):
    if i % multiplo == 0:
        print(i)