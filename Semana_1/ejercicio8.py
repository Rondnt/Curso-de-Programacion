#Escriba un programa que pida dos números enteros. El programa pedirá de nuevo el segundo número mientras no sea mayor que el primero. El programa terminará escribiendo los dos números.
print('Ingrese dos números enteros\n')

def ingresar_numero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print('Entrada inválida. Por favor, ingrese un número entero.')


num1 = ingresar_numero('Ingrese el primer número entero: ')
num2 = ingresar_numero('Ingrese el segundo número entero: ')

while num2 >= num1:
    print('El segundo número debe ser mayor que el primero')
    num2 = ingresar_numero('Ingrese el segundo número entero: ')

print(f'Los números ingresados son: {num1} y {num2}')