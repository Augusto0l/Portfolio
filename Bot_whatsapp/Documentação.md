
# Bot de Automação no WhatsApp com Python

Este projeto é um exemplo simples de automação utilizando Python para agendar e enviar mensagens pelo WhatsApp Web. A aplicação usa a biblioteca `pywhatkit`, que permite automatizar o envio de mensagens para um número específico em um horário programado.

## Objetivo do Projeto

O objetivo deste projeto é praticar conceitos de automação com Python, utilizando bibliotecas externas para executar tarefas repetitivas de forma automática. Neste caso, o sistema agenda o envio de uma mensagem pelo WhatsApp Web com base no horário atual do computador.

## Funcionalidades

- Envio automático de mensagem pelo WhatsApp;
- Agendamento da mensagem para alguns minutos após a execução do código;
- Uso da data e hora atual do sistema;
- Integração com o WhatsApp Web por meio do navegador.

## Tecnologias Utilizadas

- Python
- Biblioteca `pywhatkit`
- Biblioteca `datetime`
- WhatsApp Web

## Como Funciona

O programa define um número de telefone no formato internacional, cria uma mensagem personalizada e calcula o horário atual do sistema. Em seguida, adiciona um minuto ao horário atual para permitir que o navegador seja aberto e o WhatsApp Web seja carregado corretamente.

Depois disso, a função `sendwhatmsg()` da biblioteca `pywhatkit` é utilizada para agendar o envio da mensagem.

## Exemplo de Uso

```python
import pywhatkit as kit
import datetime

numero = "+55DDDNUMERO"
mensagem = "Olá! Esse é um bot testando automação no WhatsApp."

agora = datetime.datetime.now()
hora = agora.hour
minuto = agora.minute + 1

kit.sendwhatmsg(numero, mensagem, hora, minuto)

print("Mensagem agendada com sucesso!")
