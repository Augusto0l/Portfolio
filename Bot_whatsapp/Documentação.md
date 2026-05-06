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

## Requisitos e Como Rodar o Código

Para executar este projeto, é necessário ter o Python instalado no computador e estar conectado à internet. Também é importante estar logado no WhatsApp Web no navegador padrão, pois a automação depende dele para realizar o envio da mensagem.

Primeiro, instale a biblioteca `pywhatkit` com o comando abaixo:

```bash
pip install pywhatkit
```

Depois, abra o arquivo do projeto em uma IDE ou editor de código, como VS Code, PyCharm ou outro de sua preferência.

Antes de executar, altere o número de telefone no código para o número desejado, utilizando o formato internacional:

```python
numero = "+55DDDNUMERO"
```

Em seguida, execute o arquivo Python pelo terminal com o comando:

```bash
python nome_do_arquivo.py
```

Ao executar o programa, o navegador será aberto automaticamente com o WhatsApp Web. Após o carregamento da página, a mensagem será enviada para o número definido no código, no horário programado.

## Observações

Por segurança e privacidade, recomenda-se não deixar números de telefone reais expostos no repositório público. O ideal é substituir o número real por um exemplo genérico, como:

```python
numero = "+55DDDNUMERO"
```

Dessa forma, evita-se a exposição de dados pessoais no GitHub.

## Possíveis Melhorias Futuras

- Permitir que o usuário informe o número e a mensagem pelo terminal;
- Criar uma lista de contatos para envio automático;
- Adicionar tratamento de erros;
- Permitir agendamento para datas e horários específicos;
- Criar uma interface gráfica simples para facilitar o uso da aplicação.

## Autor

Projeto desenvolvido por Pedro como prática de automação com Python.
