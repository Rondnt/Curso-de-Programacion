#Escriba un programa que pida un año y que escriba si es bisiesto o no. Se recuerda que los años bisiestos son múltiplos de 4, pero los múltiplos de 100 no lo son, aunque los múltiplos de 400 sí.
print('Años bisiestos\n')

def ingresar_numero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")


año = ingresar_numero('Ingrese un año: ')

if año % 4 == 0 and año % 100 != 0 or año % 400 == 0:
    print(f'{año} es un año bisiesto')

else:
    print(f'{año} no es un año bisiesto')