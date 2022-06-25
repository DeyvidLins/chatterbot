from datetime import date

def criacao_arquivo_temporario_treinamento_ia(texto):
    arquivo_temp_train_ia = open("arquivo-temporario-treinamento-ia.txt", "w")
    lista_arquivo_programa = []
    lista_verificar_texto_recebido = ["Despertar", "Desperte", "Marcar", "Marque", "Alarme", "Alarmar", "Tocar",
                                      "Toque", "Agendar", "Agende"]

    hj = date.today()
    convert_string = str(hj)
    ano = convert_string[0:4]  # Ano
    mes = convert_string[6:7]  # Mês
    dia = convert_string[8:10]  # Dia
    data = dia + " do " + mes + " de " + ano

    arquivo_temp_train_ia.write(f'{texto}\n')  # Inserção da frase, para depois procurar os nomes dos programas dentro do arquivo criado.

    if "Abrir" in texto:
        resposta = texto.replace(f"{texto[:6]}", "Abrindo ")  # Recebe o texto e muda à primeira frase
        arquivo_temp_train_ia.write(f'{resposta}\n')
    elif "Data" in texto:
        arquivo_temp_train_ia.write(f'{data}\n')
    else:
        for i in lista_verificar_texto_recebido:
            if i in texto:
                arquivo_temp_train_ia.write('Ok, irá tocar conforme solicitado\n')

    arquivo_temp_train_ia.close()

    arquivo_temp_train_ia = open("arquivo-temporario-treinamento-ia.txt", "r")
    for frase in arquivo_temp_train_ia.readlines():
        lista_arquivo_programa.append(frase.replace("\n", ""))

    return lista_arquivo_programa