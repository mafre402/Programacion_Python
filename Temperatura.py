# Solicitar al usuario la temperatura en Celsius
celsius = float(input("Ingresa la temperatura en grados Celsius: "))

# Convertir a Fahrenheit usando la fórmula: F = (C × 9/5) + 32
fahrenheit = (celsius * 9/5) + 32

# Mostrar el resultado
print(f"{celsius}°C equivale a {fahrenheit}°F")