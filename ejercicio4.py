#Escriba un programa que pida dos números enteros y que escriba si el mayor es múltiplo del menor
print('Ingrese dos números enteros\n')

num1 = int(input('Ingrese el primer número entero: '))
num2 = int(input('Ingrese el segundo número entero: '))

if num1 > num2:
    if num1 % num2 == 0:
        print(f'{num1} es múltiplo de {num2}')
    else:
        print(f'{num1} no es múltiplo de {num2}')

elif num2 > num1:
    if num2 % num1 == 0:
        print(f'{num2} es múltiplo de {num1}')
    else:
        print(f'{num2} no es múltiplo de {num1}')

