#Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
print('Ingrese los lados del triangulo\n')

a = float(input('Ingrese el lado a: '))
b = float(input('Ingrese el lado b: '))

hipotenusa = (a**2 + b**2)**0.5

print(f'La hipotenusa del triangulo es: {hipotenusa:.2f}')