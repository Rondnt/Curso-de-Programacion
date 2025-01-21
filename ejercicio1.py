#José es administrador en una fábrica de chocolates, una de sus tareas es pedir las cajas al proveedor
#semanalmente, en cada caja entran 12 chocolates. Hacer un programa que le pida al jefe de producción
#la cantidad de chocolates que se producirán diariamente la próxima semana y resolver ¿qué debe hacer José?
chocolates_diarios = []

print('INVENTARIO DE PRODUCCIÓN DE CHOCOLATES \n')
print('Ingrese la cantidad de chocolates que se producirán la próxima semana:  ','\n')

for dia in ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']:
    cantidad = int(input(f'{dia}: '))
    chocolates_diarios.append(cantidad)

total_chocolates = sum(chocolates_diarios)

capacidad_caja = 12
cajas_necesarias = total_chocolates // capacidad_caja
chocolates_sobrantes = total_chocolates % capacidad_caja

if chocolates_sobrantes > 0:
    cajas_necesarias += 1

print('\nProducción de Chocolates')
print(f'\nCantidad total de chocolates producidos semanalmente: {total_chocolates}')
print(f'Número de cajas necesarias: {cajas_necesarias}')
print(f'Chocolates sobrantes: {chocolates_sobrantes}')
