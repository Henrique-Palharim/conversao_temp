c = float(input("Digite a temperatura em Celsius: "))
print("=== Convertendo temperatura em graus Celsius para Farenheit e Kelvin ===")

f = (c * 9/5) + 32
k = c + 273.15

print(f"\nTemperatura em Celsius: {c} °C")
print(f"Temperatura em Farenheit: {f} °F")
print(f"Temperatura em Kelvin: {k} K")