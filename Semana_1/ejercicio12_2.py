#Escriba una función que reciba dos números y determine si el primero es múltiplo del segundo.
#FUNCION PARA DETERMINAR MULTIPLOS DE DOS NUMEROS

def es_multiplo(num1, num2):
    if num2 == 0:
        return 'El segundo número no puede ser 0.'
    return num1 % num2 == 0

# Prueba
num1 = int(input('Ingrese el primer número: '))
num2 = int(input('Ingrese el segundo número: '))
if es_multiplo(num1, num2):
    print(f'{num1} es múltiplo de {num2}.')
else:
    print(f'{num1} no es múltiplo de {num2}.')
