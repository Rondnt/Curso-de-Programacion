#Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius. Recordar que la fórmula para la conversión es: C = (F-32)*5/9
print('Conversor de Temperatura de grados Fahrenheit a grados Celsius\n')

fahrenheit = float(input('Ingrese la temperatura en grados Fahrenheit: '))

celsius = (fahrenheit-32)*5/9

print(f'La temperatura en grados Celsius es: {celsius:.2f}')