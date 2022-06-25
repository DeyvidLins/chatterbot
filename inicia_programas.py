import os
from os import listdir

# Variáveis do caminho da pasta
pastas_01 = r'C:\Program Files'
pastas_02 = r'C:\Program Files (x86)'

# Nomes das pastas
lista_pasta_01 = [arq for arq in listdir(pastas_01)]
lista_pasta_02 = [arq for arq in listdir(pastas_02)]

programas = [] # lista vazia que vai receber os nomes das pastas

arquivo = open("nome-programas.txt", "w") # Criação do arquivo .txt para receber os nomes das pastas


class Programas:
    def __init__(self,texto):
        self.texto = texto

    def start_programas(self):
        # Se à variável texto receber Finalizar ou Encerrar o programa encerrar
        '''if texto == 'Finalizar' or 'Encerrar': #Observação.: MELHORAR
            exit()'''

        #Procura o nome do programa e realiza o start
        for pasta in lista_pasta_01:
            programas.append(pasta)

        for pasta in lista_pasta_02:
            programas.append(pasta)

        lista_unica = list(set(programas))  # remove os valores duplicados

        for prog in lista_unica:
            arquivo.write(f'{prog}\n')

        arquivo.close()
        contador = 0

        # Melhorar às estruturas de condições
        if "Abrir" in self.texto :
            while contador <= len(lista_unica):
                nome_programa = self.texto[6:]
                if nome_programa == lista_unica[contador]:
                    if nome_programa == 'Google':
                        os.system(f" Start chrome")
                        import chatboot # MELHORAR

                    elif nome_programa == 'Adobe':
                        os.system(f" Start Acrobat")
                        import chatboot # MELHORAR

                    else:
                        os.system(f" Start {nome_programa}")
                        import chatboot # MELHORAR
                contador += 1

