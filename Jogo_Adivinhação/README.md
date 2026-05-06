# Jogo de Adivinhação com Python

Este projeto é um jogo simples de adivinhação de números desenvolvido em Python. A aplicação permite que o usuário defina um número máximo para o desafio e tente adivinhar qual número aleatório foi gerado pelo programa.

## Objetivo do Projeto

O objetivo deste projeto é praticar conceitos fundamentais de programação com Python, como entrada de dados, validação de informações, geração de números aleatórios, estruturas condicionais, laços de repetição e controle de fluxo. Neste caso, o sistema gera um número aleatório e orienta o usuário até que ele consiga acertar.

## Funcionalidades

- Permite que o usuário defina o número limite do desafio;
- Gera um número aleatório dentro do intervalo definido;
- Recebe tentativas do usuário pelo terminal;
- Valida se os valores informados são numéricos;
- Informa se o chute foi maior ou menor que o número correto;
- Conta o número de tentativas realizadas;
- Permite iniciar uma nova partida após o término do jogo;
- Limpa a tela ao iniciar uma nova rodada.

## Tecnologias Utilizadas

- Python
- Biblioteca `random`
- Biblioteca `os`

## Como Funciona

O programa inicia exibindo uma mensagem de boas-vindas e solicita que o usuário informe o número teto do desafio. Esse valor será usado como limite máximo para gerar um número aleatório.

Após validar se o valor informado é numérico, o programa utiliza a função `random.randint()` para gerar um número aleatório entre `0` e o número escolhido pelo usuário.

Em seguida, o jogador começa a tentar adivinhar o número. A cada tentativa, o programa verifica se o valor digitado é válido e compara o chute com o número gerado. Caso o chute seja maior que o número correto, o sistema informa que o número aleatório é menor. Caso o chute seja menor, o sistema informa que o número aleatório é maior.

Quando o usuário acerta o número, o programa exibe uma mensagem de acerto, mostra a quantidade de tentativas realizadas e pergunta se o jogador deseja jogar novamente. Se a resposta for `sim`, uma nova partida é iniciada.

## Requisitos e Como Rodar o Código

Para executar este projeto, é necessário ter o Python instalado no computador. As bibliotecas `random` e `os` já fazem parte da biblioteca padrão do Python, portanto não é necessário instalar dependências externas.

Depois, abra o arquivo do projeto em uma IDE ou editor de código, como VS Code, PyCharm ou outro de sua preferência.

Em seguida, execute o arquivo Python pelo terminal com o comando:

```bash
python nome_do_arquivo.py
```

Ao executar o programa, informe o número máximo do desafio quando solicitado:

```bash
Digite o numero teto do desafio: 100
```

Depois, digite suas tentativas até acertar o número gerado pelo programa:

```bash
Adivinhe o número: 50
```

Ao final da partida, o programa exibirá a quantidade de tentativas e perguntará se você deseja jogar novamente.

## Possíveis Melhorias Futuras

- Corrigir acentuação das mensagens exibidas no terminal;
- Permitir escolher níveis de dificuldade;
- Definir um número máximo de tentativas;
- Exibir um histórico das tentativas do jogador;
- Adicionar pontuação com base na quantidade de tentativas;
- Melhorar a compatibilidade da limpeza de tela em diferentes sistemas operacionais;
- Criar uma interface gráfica simples para o jogo.

## Autor

Projeto desenvolvido por Pedro como prática de lógica de programação com Python.
