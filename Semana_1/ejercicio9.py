#Escriba un programa que pida números enteros mientras sean cada vez más grandes.
print('Ingrese números enteros cada vez más grandes.\n')

primer_numero = int(input('Ingrese el primer número: '))

while True:
    segundo_numero = int(input('Ingrese el siguiente número: '))

    if segundo_numero <= primer_numero:
        print('El número ingresado no es mayor')
        break

    primer_numero = segundo_numero
