from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import speech_recognition as sr # Speech regocnition
# speech synthesis
import pyttsx3
import funcoes_extra_ia
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
    arquivo_programa = open("nome-programas.txt", "w")
    lista_arquivo_programa = []

    #Loop para continuar interagindo com o usuário
    while True:
        print('Diga algo: ')
        audio = microfone.listen(fonte)  #Ouve o que o usuário vai falar

        try:
            texto = microfone.recognize_google(audio, language='pt-BR') # Reconhece o audio/voz do usuário em português
            print('Você disse: ' + texto.capitalize())


            arquivo_programa.write(f'{texto}\n') # Inserção da frase, para depois procurar o nome do programa

            resposta = texto.replace(f"{texto[:6]}","Abrindo ") # Recebe o texto e muda à primeira frase
            arquivo_programa.write(f'{resposta}\n')
            arquivo_programa.close()

            arquivo_programa = open("nome-programas.txt", "r")
            for frase in arquivo_programa.readlines():
                lista_arquivo_programa.append(frase.replace("\n",""))

            trainer.train(lista_arquivo_programa) # Novo treinamento - Recebe à lista dos nomes dos programas como parâmetro

            if (texto.capitalize()) or (texto.upper()) or (texto.lower()) or (texto.title()) in lista:
                 response = bot.get_response(texto)
                 print('Bot: ', response)
                 Speak(response)
                 funcoes_extra_ia.function(texto)
                 continue

            else:
                response = bot.get_response("não consta na base de dados")
                print('Bot: ', response)
                Speak(response)

            if qtd_falha_audio == 3:  # Contabiliza à quatidade de vezes que recebeu o valor nulo(Houve falha de comunição entre o usuário e a I.A) e encerra à conversação
                response = bot.get_response("audio ruim")
                print('Bot: ', response)
                Speak(response)
                break

        except sr.UnknownValueError:
            texto = 'null'
            qtd_falha_audio+=1
            response = bot.get_response(texto) #Caso o ambiente tenha ruído ou o usuário não diga nada, à I.A recebe um valor nulo.
            print('Bot: ', response)
            Speak(response)


