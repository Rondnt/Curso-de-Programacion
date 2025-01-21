#El usuario ingresará un número de horas, de minutos y segundos y nos devuelva el equivalente en segundos.
#FUNCION PARA CONVERTIR A SEGUNDOS

def convertir_a_segundos(horas, minutos, segundos):
    total_segundos = horas * 3600 + minutos * 60 + segundos
    return total_segundos

horas = int(input('Ingrese el número de horas: '))
minutos = int(input('Ingrese el número de minutos: '))
segundos = int(input('Ingrese el número de segundos: '))
print(f'El equivalente en segundos es: {convertir_a_segundos(horas, minutos, segundos)} segundos.')
