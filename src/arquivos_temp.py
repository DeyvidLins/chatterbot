from horas_dias_semana_data import verificar_data
from horas_dias_semana_data import verificar_dias_semana

def criacao_arquivo_temporario_treinamento_ia(texto):
    arquivo_temp_train_ia = open("arquivo-temporario-treinamento-ia.txt", "w")
    lista_arquivo_programa = []
    lista_verificar_texto_recebido = ["Despertar", "Desperte", "Marcar", "Marque", "Alarme", "Alarmar", "Tocar",
                                      "Toque", "Agendar", "Agende"]

    arquivo_temp_train_ia.write(f'{texto}\n')  # Inserção dos textos/frases de um arquivo temporário, para treinamento da IA

    if "abrir" in texto.lower():
        resposta = texto.replace(f"{texto[:6]}", "Abrindo ")  # Recebe o texto e muda à primeira frase
        arquivo_temp_train_ia.write(f'{resposta}\n')
    elif "data" in texto.lower():
        arquivo_temp_train_ia.write(f'{verificar_data()}\n')
    elif "tempo" in texto.lower():
        arquivo_temp_train_ia.write(f'A previsão do tempo é: ') # MELHORAR
    elif "semana" in texto.lower():
        arquivo_temp_train_ia.write(f'Hoje é: {verificar_dias_semana()}')
    else:
        for i in lista_verificar_texto_recebido:
            if i in texto:
                arquivo_temp_train_ia.write('Ok, irá tocar conforme solicitado\n')

    arquivo_temp_train_ia.close()

    arquivo_temp_train_ia = open("arquivo-temporario-treinamento-ia.txt", "r")
    for frase in arquivo_temp_train_ia.readlines():
        lista_arquivo_programa.append(frase.replace("\n", ""))

    return lista_arquivo_programa