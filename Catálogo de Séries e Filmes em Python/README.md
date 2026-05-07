# Catálogo de Séries e Filmes com Python, Tkinter e SQLite

## Descrição

Este projeto é um **Catálogo de Séries e Filmes** desenvolvido em **Python**, utilizando **Tkinter** para a criação da interface gráfica e **SQLite** para o armazenamento dos dados.

O sistema permite cadastrar, listar, atualizar e excluir registros de filmes e séries. Cada registro possui informações como título, tipo, ano de lançamento e gênero. Os dados são armazenados em um banco de dados local chamado `catalogo.db`, criado automaticamente ao executar o programa.

O projeto é uma aplicação desktop simples, com foco em demonstrar conceitos de **CRUD**, **interface gráfica**, **banco de dados local**, **relacionamento entre tabelas** e **normalização de textos**.

## Objetivo do Projeto

O objetivo deste projeto é desenvolver um sistema desktop para gerenciar um catálogo de filmes e séries.

A aplicação foi criada com a finalidade de praticar:

- Manipulação de banco de dados com SQLite;
- Criação de interface gráfica com Tkinter;
- Cadastro, listagem, atualização e exclusão de dados;
- Relacionamento entre tabelas;
- Organização do código com classes;
- Validação e padronização de entradas do usuário;
- Uso de chave estrangeira entre tabelas;
- Normalização de texto para remover acentos e facilitar buscas.

## Funcionalidades

O sistema possui as seguintes funcionalidades:

- Cadastro de filmes e séries;
- Listagem de filmes e séries cadastrados;
- Atualização de registros pelo ID;
- Exclusão de registros pelo ID;
- Listagem dos gêneros disponíveis;
- Associação de filmes e séries a um gênero;
- Inserção automática de gêneros iniciais;
- Validação do tipo informado, aceitando apenas `Filme` ou `Série`;
- Normalização de texto para aceitar entradas com ou sem acento;
- Exibição dos registros em uma lista na interface;
- Banco de dados criado automaticamente ao iniciar o sistema.

## Tecnologias Utilizadas

As principais tecnologias utilizadas no projeto foram:

- **Python**: linguagem principal do projeto;
- **Tkinter**: biblioteca utilizada para criar a interface gráfica;
- **SQLite**: banco de dados local utilizado para armazenar os dados;
- **sqlite3**: biblioteca nativa do Python para conexão com o SQLite;
- **unicodedata**: biblioteca utilizada para normalizar textos e remover acentos;
- **Listbox**: componente do Tkinter usado para exibir os registros cadastrados;
- **messagebox**: recurso do Tkinter utilizado para exibir mensagens de sucesso e erro.

## Como Funciona

Ao executar o programa, o sistema cria uma janela chamada **Catálogo de Séries e Filmes**.

Na interface, o usuário encontra campos para informar:

- ID;
- Título;
- Tipo;
- Ano de lançamento;
- Gênero.

O campo **ID** é utilizado apenas para atualizar ou excluir registros existentes.

O usuário pode cadastrar um novo filme ou série preenchendo título, tipo, ano e gênero. O gênero informado precisa existir previamente no banco de dados.

O sistema já inicia com alguns gêneros cadastrados automaticamente:

- Ação;
- Comédia;
- Drama;
- Terror;
- Animação.

O usuário também pode clicar no botão **Listar Gêneros** para visualizar todos os gêneros disponíveis.

## Estrutura do Banco de Dados

O banco de dados utilizado pelo sistema se chama `catalogo.db`.

Ele possui duas tabelas principais:

### Tabela `genero`

Responsável por armazenar os gêneros disponíveis para filmes e séries.

Campos da tabela:

| Campo | Tipo | Descrição |
|---|---|---|
| `id` | INTEGER | Identificador único do gênero, gerado automaticamente |
| `nome` | TEXT | Nome do gênero |

O campo `nome` possui restrição `UNIQUE`, impedindo que o mesmo gênero seja cadastrado mais de uma vez.

### Tabela `serie_filme`

Responsável por armazenar os filmes e séries cadastrados no sistema.

Campos da tabela:

| Campo | Tipo | Descrição |
|---|---|---|
| `id` | INTEGER | Identificador único do registro, gerado automaticamente |
| `titulo` | TEXT | Título do filme ou série |
| `tipo` | TEXT | Tipo do registro, podendo ser `Filme` ou `Série` |
| `ano_lancamento` | INTEGER | Ano de lançamento do filme ou série |
| `id_genero` | INTEGER | ID do gênero relacionado ao registro |

O campo `id_genero` faz a ligação entre a tabela `serie_filme` e a tabela `genero`.

## Relação entre Séries, Filmes e Gêneros

O sistema utiliza uma chave estrangeira para relacionar os filmes e séries aos seus gêneros.

A tabela `serie_filme` possui o campo `id_genero`, que faz referência ao campo `id` da tabela `genero`.

Dessa forma, cada filme ou série pertence a um gênero específico.

Exemplo:

| Título | Tipo | Ano | Gênero |
|---|---|---|---|
| Vingadores | Filme | 2012 | Ação |
| Stranger Things | Série | 2016 | Terror |
| Shrek | Filme | 2001 | Animação |

Essa relação permite que o sistema liste os registros mostrando o nome do gênero em vez de exibir apenas o ID.

## Principais Funções do Sistema

### `normalizar_texto(texto)`

Essa função recebe um texto e faz sua normalização.

Ela transforma o texto em letras minúsculas e remove acentos.

Exemplo:

| Entrada | Resultado |
|---|---|
| `Ação` | `acao` |
| `Série` | `serie` |
| `COMÉDIA` | `comedia` |

Essa função ajuda o sistema a comparar textos mesmo quando o usuário digita com ou sem acento.

### `normalizar_tipo(texto)`

Essa função valida e padroniza o tipo informado pelo usuário.

Ela aceita entradas como:

- `Filme`;
- `filme`;
- `Série`;
- `Serie`;
- `serie`.

Depois, retorna o valor padronizado como `Filme` ou `Série`.

Caso o usuário digite um tipo inválido, o sistema exibe uma mensagem de erro.

### Classe `Banco`

A classe `Banco` é responsável por toda a comunicação com o banco de dados SQLite.

Ela cria a conexão com o banco `catalogo.db` e executa as operações de criação, inserção, listagem, atualização e exclusão de dados.

### `create_tables()`

Essa função cria as tabelas `genero` e `serie_filme`, caso elas ainda não existam.

Ela garante que o banco de dados esteja preparado para armazenar os dados do sistema.

### `inserir_genero(nome)`

Essa função insere um novo gênero na tabela `genero`.

Ela utiliza `INSERT OR IGNORE`, evitando erro caso o gênero já esteja cadastrado.

### `listar_generos()`

Essa função retorna todos os gêneros cadastrados no banco de dados.

Os gêneros são exibidos na interface quando o usuário clica no botão **Listar Gêneros**.

### `buscar_genero_por_nome(nome)`

Essa função busca um gênero pelo nome informado pelo usuário.

A busca utiliza texto normalizado, permitindo encontrar gêneros mesmo quando o usuário digita sem acento ou com letras maiúsculas.

Exemplo:

| Entrada do usuário | Gênero encontrado |
|---|---|
| `acao` | Ação |
| `AÇÃO` | Ação |
| `comedia` | Comédia |

### `inserir_serie_filme(titulo, tipo, ano, id_genero)`

Essa função cadastra um novo filme ou série no banco de dados.

Ela recebe o título, o tipo, o ano de lançamento e o ID do gênero relacionado.

### `listar_series_filmes()`

Essa função lista todos os filmes e séries cadastrados.

Ela utiliza `JOIN` entre as tabelas `serie_filme` e `genero`, permitindo exibir o nome do gênero junto com cada registro.

### `atualizar_serie_filme(id, titulo, tipo, ano, id_genero)`

Essa função atualiza um registro existente com base no ID informado.

Ela permite alterar o título, o tipo, o ano de lançamento e o gênero de um filme ou série.

### `excluir_serie_filme(id)`

Essa função exclui um filme ou série do banco de dados com base no ID informado.

## Interface Gráfica

A interface gráfica é criada pela classe `Aplicacao`.

Ela contém os seguintes campos:

| Campo | Função |
|---|---|
| `ID` | Usado para atualizar ou excluir um registro |
| `Título` | Recebe o nome do filme ou série |
| `Tipo` | Define se o registro é um Filme ou uma Série |
| `Ano de Lançamento` | Recebe o ano de lançamento |
| `Gênero` | Recebe o nome do gênero relacionado |

A interface também possui os seguintes botões:

| Botão | Função |
|---|---|
| `Inserir` | Cadastra um novo filme ou série |
| `Atualizar` | Atualiza um registro existente |
| `Excluir` | Exclui um registro pelo ID |
| `Listar` | Lista todos os filmes e séries cadastrados |
| `Listar Gêneros` | Exibe os gêneros disponíveis |

Os registros são exibidos em uma área de listagem usando o componente `Listbox`.

## Validações Implementadas

O sistema possui validações básicas para evitar erros durante o uso.

Entre elas:

- Verifica se o tipo informado é `Filme` ou `Série`;
- Aceita o tipo `Série` mesmo sem acento, como `Serie`;
- Converte o ano de lançamento para número inteiro;
- Verifica se o gênero informado existe no banco de dados;
- Exibe mensagem de erro caso o gênero não seja encontrado;
- Exibe mensagem de erro caso o usuário informe dados inválidos;
- Normaliza textos para facilitar comparações;
- Evita cadastro duplicado de gêneros iniciais.

## Requisitos

Para executar o projeto, é necessário ter instalado:

- Python 3.x

As bibliotecas utilizadas já fazem parte da instalação padrão do Python:

- `sqlite3`
- `tkinter`
- `unicodedata`

Por isso, normalmente não é necessário instalar bibliotecas externas.

## Como Rodar o Código

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

### 2. Acesse a pasta do projeto

```bash
cd seu-repositorio
```

### 3. Execute o arquivo Python

```bash
python catalogo_series_filmes.py
```

Ou, dependendo da configuração do seu computador:

```bash
python3 catalogo_series_filmes.py
```

### 4. Use o sistema

Após executar o arquivo, a janela do sistema será aberta.

O banco de dados `catalogo.db` será criado automaticamente na mesma pasta do projeto.

## Exemplo de Uso

Um exemplo básico de uso do sistema seria:

1. Executar o programa;
2. Clicar em **Listar Gêneros** para verificar os gêneros disponíveis;
3. Preencher o campo **Título** com o nome do filme ou série;
4. Informar o campo **Tipo** como `Filme` ou `Série`;
5. Informar o ano de lançamento;
6. Informar um gênero existente, como `Ação`, `Comédia`, `Drama`, `Terror` ou `Animação`;
7. Clicar em **Inserir**;
8. Clicar em **Listar** para visualizar os registros cadastrados.

Exemplo de cadastro:

| Campo | Valor |
|---|---|
| Título | Vingadores |
| Tipo | Filme |
| Ano de Lançamento | 2012 |
| Gênero | Ação |

Resultado esperado na listagem:

| ID | Título | Tipo | Ano | Gênero |
|---|---|---|---|---|
| 1 | Vingadores | Filme | 2012 | Ação |

## Estrutura Sugerida do Projeto

```text
catalogo-series-filmes/
│
├── catalogo_series_filmes.py
├── catalogo.db
└── README.md
```

O arquivo `catalogo.db` é criado automaticamente após a primeira execução do sistema.

Caso queira disponibilizar o projeto no GitHub, é possível adicionar o banco de dados ao `.gitignore`, para que cada usuário gere seu próprio banco local.

Exemplo de `.gitignore`:

```text
*.db
__pycache__/
```

## Possíveis Melhorias Futuras

Algumas melhorias que podem ser implementadas futuramente são:

- Adicionar botão para cadastrar novos gêneros pela interface;
- Validar se o campo título está vazio;
- Validar se o ano de lançamento é um número positivo;
- Impedir atualização de ID inexistente;
- Impedir exclusão de ID inexistente;
- Adicionar confirmação antes de excluir um registro;
- Criar filtros por gênero;
- Criar busca por título;
- Melhorar o layout visual da interface;
- Substituir `Listbox` por `Treeview` para exibir os dados em colunas;
- Separar o código em arquivos diferentes, como banco de dados, interface e funções auxiliares;
- Fechar a conexão com o banco ao encerrar o programa;
- Adicionar campo de avaliação para filmes e séries;
- Criar relatório com quantidade de registros por gênero.

## Autor

Desenvolvido por **Pedro Augusto**.

Projeto acadêmico desenvolvido para prática de programação em Python, banco de dados SQLite, interface gráfica com Tkinter e relacionamento entre tabelas.
