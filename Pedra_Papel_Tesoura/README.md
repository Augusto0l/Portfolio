# Pedra, Papel e Tesoura com Python

Este projeto é um jogo simples de Pedra, Papel e Tesoura desenvolvido em Python. A aplicação permite que o usuário jogue contra o computador pelo terminal, acumulando pontos a cada rodada até decidir sair da partida.

## Objetivo do Projeto

O objetivo deste projeto é praticar conceitos básicos de programação com Python, como entrada de dados, estruturas condicionais, laços de repetição, geração de escolhas aleatórias e controle de pontuação. Neste caso, o sistema simula uma partida de Pedra, Papel e Tesoura entre o usuário e o computador.

## Funcionalidades

- Permite jogar Pedra, Papel e Tesoura contra o computador;
- Recebe a escolha do usuário pelo terminal;
- Gera automaticamente a escolha do computador;
- Compara as escolhas para definir o vencedor da rodada;
- Registra a pontuação do usuário;
- Registra a pontuação do computador;
- Permite encerrar a partida digitando `Q`;
- Exibe o vencedor final ao término do jogo;
- Permite iniciar uma nova partida após o encerramento.

## Tecnologias Utilizadas

- Python
- Biblioteca `random`
- Biblioteca `os`

## Como Funciona

O programa inicia perguntando ao usuário sua escolha entre Pedra, Tesoura ou Papel, utilizando as letras `R`, `T` e `P`. O usuário também pode digitar `Q` para sair da partida.

A cada rodada, o computador escolhe uma opção aleatória entre pedra, tesoura e papel. Essa escolha é feita com o auxílio da biblioteca `random`, que gera um número aleatório utilizado para selecionar uma das opções disponíveis.

Depois disso, o programa compara a escolha do usuário com a escolha do computador. Se as duas escolhas forem iguais, ocorre empate. Caso contrário, o sistema verifica as combinações vencedoras do usuário: pedra vence tesoura, papel vence pedra e tesoura vence papel.

A cada vitória, o ponto é adicionado ao jogador correspondente. Quando o usuário decide sair da partida, o programa exibe a pontuação final e informa se o vencedor foi o usuário, o computador ou se houve empate.

Ao final, o sistema pergunta se o usuário deseja jogar novamente. Caso a resposta seja `sim`, uma nova partida é iniciada.

## Requisitos e Como Rodar o Código

Para executar este projeto, é necessário ter o Python instalado no computador. As bibliotecas `random` e `os` já fazem parte da biblioteca padrão do Python, portanto não é necessário instalar dependências externas.

Depois, abra o arquivo do projeto em uma IDE ou editor de código, como VS Code, PyCharm ou outro de sua preferência.

Em seguida, execute o arquivo Python pelo terminal com o comando:

```bash
python nome_do_arquivo.py
```

Ao executar o programa, escolha uma das opções disponíveis:

```bash
Escolha R(Pedra)/T(Tesoura)/P(Papel) ou Q para sair:
```

As opções são:

```text
R - Pedra
T - Tesoura
P - Papel
Q - Sair da partida
```

Depois de cada rodada, o programa informará se você ganhou, perdeu ou empatou. Ao sair da partida, será exibida a pontuação final.

## Possíveis Melhorias Futuras

- Validar entradas inválidas digitadas pelo usuário;
- Exibir os nomes completos das escolhas em vez de apenas letras;
- Criar um menu inicial para o jogo;
- Definir uma quantidade máxima de rodadas;
- Adicionar sistema de melhor de três ou melhor de cinco;
- Criar uma interface gráfica simples;
- Melhorar a compatibilidade da limpeza de tela em diferentes sistemas operacionais;
- Adicionar um histórico das rodadas jogadas.

## Autor

Projeto desenvolvido por Pedro como prática de lógica de programação com Python.
