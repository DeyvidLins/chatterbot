import time
from datetime import datetime
from datetime import date


def verificar_horario():
    tempo_atual = time.strftime("%H:%M:%S")  # O sistema captura o horário atual
    return  tempo_atual

def verificar_dias_semana():
    dia_semana = (datetime.today().isoweekday())

    if dia_semana == 1:
        nome_dia_semana = 'Segunda'
    if dia_semana == 2:
        nome_dia_semana = 'Terça'
    if dia_semana == 3:
         nome_dia_semana = 'Quarta'
    if dia_semana == 4:
        nome_dia_semana = 'Quinta'
    if dia_semana == 5:
        nome_dia_semana = 'Sexta'
    if dia_semana == 6:
        nome_dia_semana = 'sábado'
    if dia_semana == 7:
        nome_dia_semana = 'Domingo'

    print(nome_dia_semana)
    return nome_dia_semana

def verificar_data():
    hj = date.today()
    convert_string = str(hj)
    ano = convert_string[0:4]  # Ano
    mes = convert_string[6:7]  # Mês
    dia = convert_string[8:10]  # Dia
    data = dia + " do " + mes + " de " + ano

    return data