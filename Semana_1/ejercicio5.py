#Mejore el programa anterior haciendo que no se acepten números negativos ni cero.
print('Ingrese dos números enteros\n')

def ingresar_numero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            if numero > 0:
                return numero
            else:
                print("Por favor, ingrese un número mayor a 0.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

num1 = ingresar_numero('Ingrese el primer número entero: ')
num2 = ingresar_numero('Ingrese el segundo número entero: ')

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
