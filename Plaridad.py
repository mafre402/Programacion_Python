# Solicitar al usuario un número
numero = float(input("Ingresa un número: "))

# Determinar su clasificación
if numero > 0:
    print(f"El número {numero} es POSITIVO.")
elif numero < 0:
    print(f"El número {numero} es NEGATIVO.")
else:
    print("El número ingresado es CERO.")