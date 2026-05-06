import pywhatkit as kit
import datetime

numero = "+55DDDNUMERO"
mensagem = "Olá! Esse é um bot testando automação no WhatsApp."

agora = datetime.datetime.now()
hora = agora.hour
minuto = agora.minute + 1

kit.sendwhatmsg(numero, mensagem, hora, minuto)

print("Mensagem agendada com sucesso!")

