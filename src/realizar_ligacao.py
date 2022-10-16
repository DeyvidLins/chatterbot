import os
from twilio.rest import Client

account_sid = "AC7135b2cd98e4d05951b5e867936f0572"
auth_token = "a321eb1752a0531d5096176b453a0152"
meu_numero = "+5581985675266"
numero_twilio = "+19126166481"

client = Client(account_sid,auth_token)



call = client.calls.create(
    to=meu_numero,
    from_=numero_twilio,
    twiml="""<Response><Say languague="pt-BR">
           <Play>alarme.wav</Play>
          </Say></Response>"""
)

print(call.sid)