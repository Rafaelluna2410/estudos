def converter_segundos(hora, minuto, segundos):
    horas_segundos = hora * 60 * 60
    minuto_segundos = minuto * 60
    soma = horas_segundos + minuto_segundos + segundos

    return soma

print(converter_segundos(1, 1, 30))