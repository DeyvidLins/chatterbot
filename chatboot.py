# Parte chatterbot
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

# Speech regocnition
import speech_recognition as sr

# speech synthesis
import pyttsx3

bot = ChatBot('Angell')

trainer = ListTrainer(bot)
speak = pyttsx3.init('sapi5')


def Speak(text):
    speak.say(text)
    speak.runAndWait()


trainer.train(['Oi',
               'Olá tudo bem com você ?',
               'Claro! e com você?',
               'Melhor agora com sua companhia!',
               'Obrigado!',
               'Eu que agradeço pela sua presença'])

r = sr.Recognizer()
with sr.Microphone() as fonte:


    while True:
        print('Diga algo: ')
        audio = r.listen(fonte)  # escutar
        texto = r.recognize_google(audio, language='pt-BR')  # fala

        try:
            print('Você disse: ' + texto.capitalize())
        except:
            print('Não foi possível compreender o áudio')

        response = bot.get_response(texto)
        print('Bot: ', response)
        Speak(response)
