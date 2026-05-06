# Quiz de Conhecimentos Gerais com Python

Este projeto é um quiz simples de conhecimentos gerais desenvolvido em Python. A aplicação apresenta uma sequência de perguntas de múltipla escolha no terminal, recebe as respostas do usuário, calcula a pontuação final e permite repetir o quiz ao final da execução.

## Objetivo do Projeto

O objetivo deste projeto é praticar conceitos básicos de programação com Python, como entrada de dados, estruturas condicionais, controle de pontuação, repetição de execução e interação com o usuário pelo terminal. Neste caso, o sistema simula um quiz de perguntas e respostas, verificando automaticamente se as alternativas escolhidas estão corretas.

## Funcionalidades

- Exibe perguntas de conhecimentos gerais no terminal;
- Apresenta alternativas de múltipla escolha;
- Recebe a resposta do usuário;
- Padroniza a resposta digitada com letras maiúsculas;
- Verifica se a alternativa escolhida está correta;
- Exibe mensagens de acerto ou erro;
- Calcula a pontuação final do usuário;
- Mostra o total de acertos ao final do quiz;
- Permite que o usuário refaça o quiz;
- Limpa a tela antes de iniciar uma nova rodada.

## Tecnologias Utilizadas

- Python
- Biblioteca `os`

## Como Funciona

O programa inicia exibindo uma mensagem de boas-vindas ao usuário e apresenta uma sequência de perguntas de conhecimentos gerais. Cada pergunta possui alternativas identificadas por letras, como `A`, `B`, `C`, `D` e, em alguns casos, `E`.

Após cada pergunta, o usuário digita a alternativa escolhida. A resposta é tratada com os métodos `strip()` e `upper()`, removendo espaços extras e convertendo a entrada para letra maiúscula. Isso facilita a comparação com a resposta correta.

Se a resposta estiver correta, o programa exibe uma mensagem de acerto e adiciona um ponto à pontuação do usuário. Caso contrário, informa que a resposta está errada e mostra a alternativa correta.

Ao final das dez perguntas, o sistema exibe a pontuação total no formato `score/10`. Depois disso, pergunta se o usuário deseja fazer o quiz novamente. Caso a resposta seja `sim`, o quiz é reiniciado.

## Requisitos e Como Rodar o Código

Para executar este projeto, é necessário ter o Python instalado no computador. A biblioteca `os` já faz parte da biblioteca padrão do Python, portanto não é necessário instalar dependências externas.

Depois, abra o arquivo do projeto em uma IDE ou editor de código, como VS Code, PyCharm ou outro de sua preferência.

Em seguida, execute o arquivo Python pelo terminal com o comando:

```bash
python nome_do_arquivo.py
```

Ao executar o programa, o quiz será iniciado no terminal e a primeira pergunta será exibida:

```bash
Bem-vindo ao Quiz de Conhecimentos Gerais
```

Para responder, digite apenas a letra correspondente à alternativa escolhida:

```bash
Resposta: C
```

Após responder todas as perguntas, o programa exibirá sua pontuação final e perguntará se você deseja jogar novamente.

## Possíveis Melhorias Futuras

- Corrigir pequenas inconsistências nas mensagens de resposta correta;
- Adicionar validação para alternativas inválidas;
- Organizar as perguntas em uma lista ou dicionário;
- Embaralhar a ordem das perguntas;
- Criar níveis de dificuldade;
- Adicionar mais perguntas ao quiz;
- Salvar a pontuação final em um arquivo;
- Criar uma interface gráfica simples;
- Melhorar a compatibilidade da limpeza de tela em diferentes sistemas operacionais.

## Autor

Projeto desenvolvido por Pedro como prática de lógica de programação com Python.
