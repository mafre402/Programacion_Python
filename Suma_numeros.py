# Programa: Suma acumulativa hasta ingresar 0
print("Suma de números (ingresa 0 para terminar)")

total = 0
contador = 0

while True:
    try:
        numero = float(input(f"Ingresa el número #{contador + 1}: "))
        
        if numero == 0:
            break  # Salir del ciclo si se ingresa 0
        
        total += numero
        contador += 1
        print(f"Suma parcial: {total:.2f}")  # Muestra acumulado con 2 decimales
        
    except ValueError:
        print("⚠️ Error: Debes ingresar un número válido. Intenta nuevamente.")

# Mostrar resultados finales
print("\n" + "="*30)
print(f"→ Total de números sumados: {contador}")
print(f"→ Suma final: {total:.2f}")
print("="*30)