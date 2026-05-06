# Contador Regressivo com Python

Este projeto é um exemplo simples de contador regressivo utilizando Python. A aplicação permite que o usuário informe um tempo em segundos e, a partir desse valor, exibe uma contagem regressiva no terminal até o tempo acabar.

## Objetivo do Projeto

O objetivo deste projeto é praticar conceitos básicos de programação com Python, como entrada de dados, validação de valores, estruturas condicionais, laços de repetição e manipulação de tempo. Neste caso, o sistema recebe um número de segundos informado pelo usuário e realiza uma contagem regressiva em formato de minutos e segundos.

## Funcionalidades

- Recebe um tempo em segundos informado pelo usuário;
- Valida se a entrada digitada é um número;
- Converte o valor informado para inteiro;
- Exibe a contagem regressiva no terminal;
- Mostra o tempo no formato de minutos e segundos;
- Finaliza a execução com uma mensagem informando que o tempo acabou.

## Tecnologias Utilizadas

- Python
- Biblioteca `time`

## Como Funciona

O programa solicita que o usuário digite um tempo em segundos. Em seguida, verifica se o valor informado contém apenas números utilizando o método `isdigit()`.

Caso a entrada seja válida, o valor é convertido para inteiro e o programa inicia um laço de repetição. Durante esse processo, a função `divmod()` é utilizada para transformar os segundos em minutos e segundos, facilitando a exibição do tempo no formato `minutos:segundos`.

A cada repetição, o programa exibe o tempo restante no terminal, aguarda um segundo com `time.sleep(1)` e diminui uma unidade do contador. Quando o tempo chega a zero, a mensagem `TEMPO ACABOU!` é exibida.

## Requisitos e Como Rodar o Código

Para executar este projeto, é necessário ter o Python instalado no computador. A biblioteca `time` já faz parte da biblioteca padrão do Python, portanto não é necessário instalar dependências externas.

Depois, abra o arquivo do projeto em uma IDE ou editor de código, como VS Code, PyCharm ou outro de sua preferência.

Em seguida, execute o arquivo Python pelo terminal com o comando:

```bash
python nome_do_arquivo.py
```

Ao executar o programa, digite o tempo desejado em segundos quando solicitado:

```bash
Digite o tempo (em segundos): 60
```

Após isso, o contador será iniciado no terminal e exibirá a contagem regressiva até o tempo acabar.

## Possíveis Melhorias Futuras

- Exibir o tempo no formato `MM:SS` com dois dígitos;
- Permitir que o usuário informe horas, minutos e segundos separadamente;
- Adicionar uma mensagem sonora ao final da contagem;
- Criar uma interface gráfica simples;
- Permitir pausar, continuar ou cancelar o contador;
- Adicionar tratamento para valores negativos ou entradas vazias.

## Autor

Projeto desenvolvido por Pedro como prática de programação com Python.
