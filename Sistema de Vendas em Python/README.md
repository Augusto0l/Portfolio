# Sistema de Vendas com Python, Tkinter e SQLite

## Descrição

Este projeto é um **Sistema de Vendas** desenvolvido em **Python**, utilizando **Tkinter** para a criação da interface gráfica e **SQLite** para o armazenamento dos dados.

O sistema permite cadastrar clientes, registrar pedidos, excluir clientes e pedidos, além de visualizar a relação entre clientes e seus respectivos pedidos. O banco de dados é criado automaticamente ao executar o programa, armazenando as informações em um arquivo local chamado `sistema_vendas.db`.

O projeto é uma aplicação simples, com foco em demonstrar conceitos de **CRUD**, **interface gráfica**, **banco de dados local** e **relacionamento entre tabelas**.

## Objetivo do Projeto

O objetivo deste projeto é desenvolver um sistema desktop simples para gerenciar clientes e pedidos de vendas.

A aplicação foi criada com a finalidade de praticar:

- Manipulação de banco de dados com SQLite;
- Criação de interface gráfica com Tkinter;
- Cadastro, listagem e exclusão de dados;
- Relacionamento entre tabelas;
- Organização de funções em Python;
- Uso de abas para separar funcionalidades dentro da interface.

## Funcionalidades

O sistema possui as seguintes funcionalidades:

- Cadastro de clientes com nome e e-mail;
- Listagem de clientes cadastrados;
- Exclusão de clientes pelo ID;
- Cadastro de pedidos vinculados a um cliente;
- Listagem de pedidos cadastrados;
- Exclusão de pedidos pelo ID;
- Visualização de clientes com seus respectivos pedidos;
- Exibição de clientes sem pedidos cadastrados;
- Mensagens de sucesso, erro e alerta para orientar o usuário;
- Banco de dados criado automaticamente ao iniciar o sistema.

## Tecnologias Utilizadas

As principais tecnologias utilizadas no projeto foram:

- **Python**: linguagem principal do projeto;
- **Tkinter**: biblioteca utilizada para criar a interface gráfica;
- **ttk**: recurso do Tkinter utilizado para criação de abas;
- **SQLite**: banco de dados local utilizado para armazenar clientes e pedidos;
- **sqlite3**: biblioteca nativa do Python para conexão com o SQLite.

## Como Funciona

Ao executar o programa, o sistema cria uma janela chamada **Sistema de Vendas**.

A interface é dividida em duas abas principais:

### 1. Cadastro e Pedidos

Nesta aba, o usuário pode cadastrar clientes informando nome e e-mail.

Também é possível cadastrar pedidos, informando:

- ID do cliente;
- Nome do produto;
- Valor do pedido.

Além disso, essa aba permite excluir clientes e pedidos pelo ID, bem como visualizar as listas de clientes e pedidos cadastrados.

### 2. Clientes e seus Pedidos

Nesta aba, o sistema exibe a relação entre os clientes cadastrados e seus pedidos.

Caso um cliente não tenha nenhum pedido registrado, o sistema mostra a mensagem **“Sem pedidos”** ao lado do nome do cliente.

## Estrutura do Banco de Dados

O banco de dados utilizado pelo sistema se chama `sistema_vendas.db`.

Ele possui duas tabelas principais:

### Tabela `clientes`

Responsável por armazenar os dados dos clientes.

Campos da tabela:

| Campo | Tipo | Descrição |
|---|---|---|
| `id` | INTEGER | Identificador único do cliente, gerado automaticamente |
| `nome` | TEXT | Nome do cliente |
| `email` | TEXT | E-mail do cliente |

O campo `id` é gerado automaticamente pelo banco de dados.

### Tabela `pedidos`

Responsável por armazenar os pedidos feitos pelos clientes.

Campos da tabela:

| Campo | Tipo | Descrição |
|---|---|---|
| `id` | INTEGER | Identificador único do pedido, gerado automaticamente |
| `cliente_id` | INTEGER | ID do cliente relacionado ao pedido |
| `produto` | TEXT | Nome do produto vendido |
| `valor` | REAL | Valor do pedido |

O campo `cliente_id` faz a ligação entre a tabela de pedidos e a tabela de clientes.

Essa relação permite saber qual cliente realizou determinado pedido.

## Relação entre Clientes e Pedidos

O sistema utiliza uma chave estrangeira para relacionar os pedidos aos clientes.

A tabela `pedidos` possui o campo `cliente_id`, que faz referência ao campo `id` da tabela `clientes`.

Dessa forma, cada pedido pertence a um cliente específico.

Exemplo:

| Cliente | Produto | Valor |
|---|---|---|
| João | Notebook | R$ 2500,00 |

Isso significa que o pedido de Notebook está vinculado ao cliente João.

## Principais Funções do Sistema

### `inserir_cliente(nome, email)`

Essa função cadastra um novo cliente no banco de dados.

Ela recebe o nome e o e-mail do cliente e salva essas informações na tabela `clientes`.

### `listar_clientes()`

Essa função busca todos os clientes cadastrados no banco de dados.

Os dados são exibidos na interface dentro da lista de clientes.

### `excluir_cliente(id_cliente)`

Essa função exclui um cliente com base no ID informado.

Caso o ID exista, o cliente é removido do banco de dados.

### `inserir_pedido(cliente_id, produto, valor)`

Essa função cadastra um novo pedido no sistema.

Ela recebe o ID do cliente, o nome do produto e o valor do pedido.

### `listar_pedidos()`

Essa função lista todos os pedidos cadastrados, mostrando também o nome do cliente relacionado ao pedido.

Para isso, o sistema utiliza um `JOIN` entre as tabelas `clientes` e `pedidos`.

### `excluir_pedido(id_pedido)`

Essa função exclui um pedido com base no ID informado.

Caso o ID exista, o pedido é removido do banco de dados.

### `listar_clientes_com_pedidos()`

Essa função mostra todos os clientes junto com seus pedidos.

Ela utiliza `LEFT JOIN`, permitindo que clientes sem pedidos também apareçam na listagem.

### `fechar_conexao()`

Essa função fecha a conexão com o banco de dados quando o programa é encerrado.

## Validações Implementadas

O sistema possui validações básicas para evitar erros durante o uso.

Entre elas:

- Impede cadastro de cliente sem nome;
- Impede cadastro de cliente sem e-mail;
- Verifica se o ID informado é válido;
- Verifica se o valor do pedido é numérico;
- Impede cadastro de pedido sem produto;
- Exibe mensagem de erro caso os dados sejam inválidos;
- Exibe mensagem caso o ID informado para exclusão não seja encontrado.

## Requisitos

Para executar o projeto, é necessário ter instalado:

- Python 3.x

As bibliotecas utilizadas já fazem parte da instalação padrão do Python:

- `tkinter`
- `sqlite3`

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
python sistema_vendas.py
```

Ou, dependendo da configuração do seu computador:

```bash
python3 sistema_vendas.py
```

### 4. Use o sistema

Após executar o arquivo, a janela do sistema será aberta.

O banco de dados `sistema_vendas.db` será criado automaticamente na mesma pasta do projeto.

## Exemplo de Uso

Um exemplo básico de uso do sistema seria:

1. Cadastrar um cliente informando nome e e-mail;
2. Verificar o ID do cliente na lista de clientes cadastrados;
3. Cadastrar um pedido usando o ID desse cliente;
4. Informar o produto e o valor do pedido;
5. Visualizar o pedido cadastrado na lista;
6. Acessar a aba **Clientes e seus Pedidos** para ver a relação entre cliente e pedido.

## Estrutura Sugerida do Projeto

```text
sistema-vendas-python/
│
├── sistema_vendas.py
├── sistema_vendas.db
└── README.md
```

O arquivo `sistema_vendas.db` é criado automaticamente após a primeira execução do sistema.

Caso queira disponibilizar o projeto no GitHub, é possível adicionar o banco de dados ao `.gitignore`, para que cada usuário gere seu próprio banco local.

Exemplo de `.gitignore`:

```text
*.db
__pycache__/
```

## Possíveis Melhorias Futuras

Algumas melhorias que podem ser implementadas futuramente são:

- Adicionar edição de clientes cadastrados;
- Adicionar edição de pedidos cadastrados;
- Criar validação mais completa para e-mails;
- Impedir cadastro de pedido para cliente inexistente;
- Melhorar o layout da interface gráfica;
- Adicionar campo de busca por cliente;
- Adicionar campo de busca por pedido;
- Criar relatórios de vendas;
- Calcular o valor total vendido;
- Exibir quantidade total de pedidos por cliente;
- Adicionar confirmação antes de excluir clientes ou pedidos;
- Melhorar a organização visual usando `grid` em vez de apenas `pack`;
- Separar o código em arquivos diferentes, como banco de dados, interface e funções principais.

## Autor

Desenvolvido por **Pedro Augusto**.

Projeto acadêmico desenvolvido para prática de programação em Python, banco de dados SQLite e interface gráfica com Tkinter.
