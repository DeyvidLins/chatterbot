from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import speech_recognition as sr
import pyttsx3
import arquivos_temp
import invoca_acoes_ia
from os import walk

bot = ChatBot('Dulce')

trainer = ListTrainer(bot)
speak = pyttsx3.init('sapi5')

def Speak(text):
    speak.say(text)
    speak.runAndWait()

arquivo = open('ler.txt', 'r')

lista = []
for item in arquivo.readlines():
    i = item.replace('\n', '')
    lista.append(i)

trainer.train(lista)

microfone = sr.Recognizer() #Microfone
with sr.Microphone() as fonte:
    microfone.adjust_for_ambient_noise(fonte)

#---------------------Saudação de Inicío---------------------------------------
    response = bot.get_response("Olá")  # Saudações da I.A
    print('Bot: ', response)
    Speak(response)
    response = bot.get_response("Diga")  # Saudações da I.A
    print('Bot: ', response)
    Speak(response)
    print('Aguardando você falar em posso ajudar: ')

    qtd_falha_audio = 0 #Contador de falhas no Áudio

    #Loop para continuar interagindo com o usuário
    while True:
        print('Diga algo: ')
        audio = microfone.listen(fonte)  #Ouve o que o usuário vai falar

        try:
            texto = microfone.recognize_google(audio, language='pt-BR') # Reconhece o audio/voz do usuário em português
            print('Você disse: ' + texto.capitalize())

            programas = arquivos_temp.criacao_arquivo_temporario_treinamento_ia(texto) # chama o método que é responsável pela criação do arquivos para um novo treinamento da IA

            trainer.train(programas)  # Novo treinamento - Recebe à lista dos nomes dos programas como parâmetro

            if (texto.capitalize()) or (texto.upper()) or (texto.lower()) or (texto.title()) in lista:
                 response = bot.get_response(texto)
                 print('Bot: ', response)
                 Speak(response)
                 invoca_acoes_ia.invoke_acoes(texto)
                 continue

            else:
                response = bot.get_response("não consta na base de dados")
                print('Bot: ', response)
                Speak(response)

        except sr.UnknownValueError:
            texto = 'null'
            qtd_falha_audio+=1
            response = bot.get_response(texto) # Caso o ambiente tenha ruído ou o usuário não diga nada, à I.A recebe um valor nulo.
            print('Bot: ', response)
            Speak(response)

            if qtd_falha_audio == 3:  # Contabiliza à quatidade de vezes que recebeu o valor nulo(Houve falha de comunição entre o usuário e a I.A) e encerra à conversação
                response = bot.get_response("Audio ruim")
                print('Bot: ', response)
                Speak(response)
                break

