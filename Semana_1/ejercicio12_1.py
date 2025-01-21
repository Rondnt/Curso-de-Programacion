#Un estacionamiento cobra S/3.00 por la primera hora, luego S/0.50 por cada hora siguiente. El cargo máximo por día es de S/12.00. Programe una función para que al ingresar el número de horas se imprima el cargo.
#FUNCION PARA INGRESAR EL NUMERO DE HORAS Y SE IMPRIMA EL CARGO

def ingresar_numero(mensaje):
    while True:
        try:
            horas = int(input(mensaje))
            return horas
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

def calcular_cargo_estacionamiento(horas):
    if horas <= 1:
        return 3.00
    else:
        cargo = 3.00 + (horas - 1) * 0.50
        return min(cargo, 12.00)

horas = ingresar_numero('Ingrese un número de horas en el estacionamiento: ')

print(f'El cargo por {horas} horas es: S/{calcular_cargo_estacionamiento(horas):.2f}')
