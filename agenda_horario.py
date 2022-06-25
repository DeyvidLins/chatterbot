import time
import playsound
from pygame import mixer

class Agenda:
    def __init__(self,texto):
        self.texto = texto

    def verificar_horario(self):
        verificar_number = self.texto.split()  # Fatia à String que foi passada e transforma em uma lista
        tempo = int(verificar_number[-2])  # Pega o valor inteiro da lista e transforma em inteiro

        tempo_atual = time.strftime("%H:%M:%S") # O sistema captura o horário atual

        cont = 0
        qtd_total = len(verificar_number) - 1

        while cont <= qtd_total:

            # Horas
            if (verificar_number[cont].lower() == 'hora') or (verificar_number[cont].lower() == 'horas'):
                incremento_hora = int(tempo_atual[0:2]) + tempo
                if incremento_hora < 23:
                    hora = tempo_atual.replace(f"{tempo_atual[0:2]}", f"{incremento_hora}")
                    compara_tempo = hora
                else:
                    horario_segundos = incremento_hora * 3600
                    verificar_horario_segundo(horario_segundos)
                    break

            # Minutos
            elif (verificar_number[cont].lower() == 'minuto') or (verificar_number[cont].lower() == 'minutos'):
                incremento_minuto = int(tempo_atual[3:5]) + tempo
                if incremento_minuto < 59:
                    minutos = tempo_atual.replace(f"{tempo_atual[3:5]}", f"{incremento_minuto}")
                    compara_tempo = minutos
                else:
                    horario_segundos = incremento_minuto * 60
                    verificar_horario_segundo(horario_segundos)
                    break

            # Segundos
            elif (verificar_number[cont].lower() == 'segundo') or (verificar_number[cont].lower() == 'segundos'):
                incremento_segundo = int(tempo_atual[6:8]) + tempo
                if incremento_segundo < 59:
                     segundos = tempo_atual.replace(f"{tempo_atual[6:8]}", f"{incremento_segundo}")
                     compara_tempo = segundos
                else:
                     horario_segundos = incremento_segundo
                     verificar_horario_segundo(horario_segundos)
                     break


            cont += 1

        print("Compara Tempo: " + compara_tempo)
        print("AGUARDANDO ALARME TOCAR...")
        while compara_tempo != tempo_atual:  # Verificar à cada segundo o horário que foi passado com o atual
            print("Tempo Atual: " + tempo_atual)
            tempo_atual = time.strftime("%H:%M:%S")
            time.sleep(1)
            if compara_tempo == tempo_atual:
                print("Reproduzindo....")
                mixer.init()
                mixer.music.load('alarme.wav')
                mixer.music.play()
                time.sleep(12)

# Caso o usuário informe um valor que não foi esperado, o alarme irá contar em segundos para poder tocar
tempo_atual = time.strftime("%H:%M:%S")
def verificar_horario_segundo(horario_segundos):
       print("AGUARDANDO ALARME TOCAR...")
       print("Tempo Atual: " + tempo_atual)
       time.sleep(horario_segundos)
       print("Reproduzindo....")
       mixer.init()
       mixer.music.load('alarme.wav')
       mixer.music.play()
       time.sleep(12)


