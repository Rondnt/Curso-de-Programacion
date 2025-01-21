#Escriba un programa que pida las notas de un grupo, se le preguntará al usuario si quiere seguir ingresando notas, y mientras la respuesta sea Sí/SÍ/sí, se debe seguir ingresando. Al finalizar el ingreso de notas, se debe mostrar una lista de las notas aprobadas y otra de las desaprobadas.
notas_aprobadas = []
notas_desaprobadas = []

print('Ingrese las notas del grupo (0 a 20).\n')

while True:

    try:
        nota = float(input('Ingrese una nota: '))
        if nota < 0 or nota > 20:
            print('Por favor, ingrese una nota válida entre 0 y 20.')
            continue
    except ValueError:
        print('Entrada inválida. Ingrese un número.')
        continue

    if nota >= 11:
        notas_aprobadas.append(nota)
    else:
        notas_desaprobadas.append(nota)

    respuesta = input('¿Desea ingresar otra nota? (Sí/No): ').strip().lower()
    if respuesta != 'sí' and respuesta != 'si':
        break


print('\nNotas aprobadas:', notas_aprobadas)
print('Notas desaprobadas:', notas_desaprobadas)
