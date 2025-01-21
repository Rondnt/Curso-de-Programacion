#Muestra los múltiplos de 3 a partir del 3 hasta el número que el usuario indique.
print('Múltiplos de 3\n')

def ingresar_numero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")


numero = ingresar_numero('Ingrese un número: ')

for i in range(3, numero+1):
    if i % 3 == 0:
        print(i)