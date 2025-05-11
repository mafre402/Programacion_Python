def ingresar_complejo():
    """Solicita al usuario las partes real e imaginaria"""
    real = float(input("Ingrese la parte real: "))
    imag = float(input("Ingrese la parte imaginaria: "))
    return complex(real, imag)

print("Suma de números complejos")
print("\nPrimer número complejo:")
c1 = ingresar_complejo()
print("\nSegundo número complejo:")
c2 = ingresar_complejo()

print(f"\nSuma: {c1} + {c2} = {c1 + c2}")