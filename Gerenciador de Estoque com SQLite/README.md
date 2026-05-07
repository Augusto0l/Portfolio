# Sistema de Controle de Estoque com Python e SQLite

## Descrição

Este projeto é um sistema simples de controle de estoque desenvolvido em Python, utilizando o SQLite como banco de dados local. O sistema funciona pelo terminal e permite cadastrar, listar, alterar e remover itens de um estoque.

A aplicação foi criada com foco no aprendizado de manipulação de banco de dados, criação de tabelas, validação de dados e operações básicas de CRUD.

## Objetivo do Projeto

O objetivo deste projeto é desenvolver um sistema de estoque funcional, capaz de armazenar informações de produtos em um banco de dados local.

Com ele, é possível praticar conceitos importantes de programação, como:

- Conexão com banco de dados;
- Criação de tabelas;
- Inserção de dados;
- Atualização de registros;
- Exclusão de itens;
- Validação de entradas do usuário;
- Uso de menu interativo no terminal.

## Funcionalidades

O sistema possui as seguintes funcionalidades:

- Cadastrar novos itens no estoque;
- Listar os itens cadastrados;
- Armazenar nome, quantidade e valor de cada item;
- Impedir o cadastro de itens com nomes repetidos;
- Validar se o nome do item é válido;
- Validar se quantidade e preço são valores numéricos;
- Alterar quantidade e preço de um item já cadastrado;
- Remover itens do estoque;
- Criar automaticamente o banco de dados e a tabela, caso ainda não existam;
- Exibir um menu interativo no terminal.

## Tecnologias Utilizadas

As principais tecnologias utilizadas no projeto foram:

- Python;
- SQLite;
- Biblioteca `sqlite3`;
- Terminal/Console.

## Como Funciona

Ao iniciar o programa, o sistema cria uma conexão com o banco de dados local chamado `meu_estoque.db`.

Em seguida, ele verifica se a tabela `itens` já existe. Caso não exista, a tabela é criada automaticamente com os seguintes campos:

```sql
id INTEGER PRIMARY KEY AUTOINCREMENT,
nome TEXT UNIQUE NOT NULL,
qtd INTEGER NOT NULL,
valor REAL NOT NULL
```

Depois disso, o usuário acessa um menu no terminal com as seguintes opções:

```text
----- CONTROLE DE ESTOQUE -----
1. Cadastrar novo item
2. Listar itens
3. Alterar item
4. Excluir item
5. Sair
```

Ao escolher uma opção, o sistema executa a ação correspondente.

Por exemplo, ao cadastrar um item, o usuário informa o nome, a quantidade e o preço do produto. Essas informações são salvas no banco de dados SQLite.

Caso o usuário tente cadastrar um item com nome repetido, o sistema exibe uma mensagem de erro. Também são feitas validações para evitar nomes vazios, nomes numéricos e valores inválidos para quantidade e preço.

## Requisitos

Para executar o projeto, é necessário ter instalado:

- Python 3;
- Um editor de código, como VS Code, PyCharm ou outro de sua preferência.

A biblioteca `sqlite3` já vem instalada por padrão junto com o Python, então não é necessário instalar pacotes externos.

## Como Rodar o Código

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/controle-estoque-python-sqlite.git
```

2. Acesse a pasta do projeto:

```bash
cd controle-estoque-python-sqlite
```

3. Execute o arquivo principal:

```bash
python main.py
```

Ou, dependendo da instalação do Python:

```bash
python3 main.py
```

4. Após executar o programa, o menu será exibido no terminal:

```text
----- CONTROLE DE ESTOQUE -----
1. Cadastrar novo item
2. Listar itens
3. Alterar item
4. Excluir item
5. Sair
```

5. Escolha a opção desejada e siga as instruções exibidas no terminal.

## Estrutura do Banco de Dados

O banco de dados utilizado no projeto é o SQLite. Ele é salvo localmente no arquivo:

```text
meu_estoque.db
```

A tabela principal do sistema se chama:

```text
itens
```

Ela possui os seguintes campos:

| Campo | Tipo | Descrição |
|---|---|---|
| id | INTEGER | Identificador único do item |
| nome | TEXT | Nome do item cadastrado |
| qtd | INTEGER | Quantidade do item em estoque |
| valor | REAL | Valor/preço do item |

## Observação Importante

No código original, existe uma chamada para a função:

```python
mostrar_itens()
```

Porém, essa função precisa estar criada no código para que a opção de listar itens funcione corretamente.

Caso ela ainda não exista, é necessário adicioná-la ao projeto.

Exemplo de função para listar os itens:

```python
def mostrar_itens():
    conexao = obter_conexao()
    cursor = conexao.cursor()
    cursor.execute("SELECT id, nome, qtd, valor FROM itens")
    itens = cursor.fetchall()

    if not itens:
        print("Nenhum item cadastrado.")
    else:
        print("\n----- ITENS CADASTRADOS -----")
        for item in itens:
            print(f"ID: {item[0]} | Nome: {item[1]} | Quantidade: {item[2]} | Preço: R$ {item[3]:.2f}")

    conexao.close()
```

## Possíveis Melhorias Futuras

Algumas melhorias que podem ser implementadas futuramente são:

- Criar uma interface gráfica para o sistema;
- Adicionar busca de itens pelo nome;
- Permitir alterar também o nome do produto;
- Criar relatórios de estoque;
- Exibir o valor total de cada item com base na quantidade;
- Exibir o valor total geral do estoque;
- Adicionar categorias para os produtos;
- Exportar os dados para uma planilha;
- Melhorar o tratamento de erros do menu;
- Criar uma versão web do sistema.

## Autor

Desenvolvido por Pedro Augusto.

Projeto criado para fins acadêmicos e prática de programação com Python e banco de dados SQLite.
