#Pedir el nombre de 5 asignaturas y su notas respectivas, luego mostrar los mensajes: “En la asignatura XXXXXXX sacó XXXXXX, para cada asignatura.
print('Registro de Notas')

asignaturas = []
notas = []

for i in range(5):
    nombre_asignatura = input(f'Ingrese el nombre de la asignatura {i + 1}: ')
    while True:
        try:
            nota = float(input(f'Ingrese la nota para {nombre_asignatura} (0 a 20): '))
            if 0 <= nota <= 20:
                break
            else:
                print('La nota debe estar entre 0 y 20')
        except ValueError:
            print('Entrada inválida. Por favor, ingrese un número.')

    asignaturas.append(nombre_asignatura)
    notas.append(nota)

print('\nResultados:')

for i in range(5):
  print(f'En la asignatura {asignaturas[i]} sacó {notas[i]:.2f}')