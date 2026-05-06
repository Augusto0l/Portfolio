# Coletor de Dados Web

Este projeto é um exemplo simples de coleta de dados na web utilizando Python. A aplicação acessa a página inicial do portal G1 e extrai os títulos das notícias disponíveis, exibindo os resultados no terminal de forma numerada.

## Objetivo do Projeto

O objetivo deste projeto é praticar conceitos básicos de web scraping com Python, utilizando requisições HTTP e análise de conteúdo HTML. O projeto permite compreender como uma aplicação pode acessar uma página da internet, interpretar sua estrutura e coletar informações específicas de forma automatizada.

## Funcionalidades

- Acessa automaticamente uma página da web;
- Realiza uma requisição HTTP para obter o conteúdo da página;
- Analisa o HTML utilizando a biblioteca `BeautifulSoup`;
- Localiza links de notícias com base em uma classe HTML específica;
- Exibe os títulos das notícias no terminal;
- Numera automaticamente cada notícia encontrada.

## Tecnologias Utilizadas

- Python
- Biblioteca `requests`
- Biblioteca `BeautifulSoup`
- HTML
- Web Scraping

## Como Funciona

O programa utiliza a biblioteca `requests` para acessar a página inicial do G1. Após receber o conteúdo HTML da página, esse conteúdo é processado com a biblioteca `BeautifulSoup`, que permite navegar e buscar elementos dentro da estrutura HTML.

Em seguida, o código procura todos os elementos `<a>` que possuem a classe `feed-post-link`, utilizada para identificar links de notícias na página. Cada notícia encontrada é percorrida em um laço de repetição e exibida no terminal com uma numeração automática.

## Requisitos e Como Rodar o Código

Para executar este projeto, é necessário ter o Python instalado no computador e estar conectado à internet, pois o programa acessa uma página web em tempo real.

Primeiro, instale as bibliotecas necessárias com o comando abaixo:

```bash
pip install requests beautifulsoup4
```

Depois, abra o arquivo do projeto em uma IDE ou editor de código, como VS Code, PyCharm ou outro de sua preferência.

Em seguida, execute o arquivo Python pelo terminal com o comando:

```bash
python nome_do_arquivo.py
```

Ao executar o programa, ele acessará o site definido no código, coletará os títulos das notícias encontradas e exibirá o resultado diretamente no terminal.

## Observações

Este projeto depende da estrutura HTML do site acessado. Caso o site altere suas classes, tags ou organização interna, pode ser necessário atualizar o código para que a coleta continue funcionando corretamente.

Além disso, o projeto foi desenvolvido com finalidade de estudo e prática de web scraping. Em aplicações reais, é importante verificar as políticas de uso do site e respeitar boas práticas de acesso automatizado.

## Possíveis Melhorias Futuras

- Permitir que o usuário informe a URL desejada;
- Salvar as notícias coletadas em um arquivo `.txt` ou `.csv`;
- Adicionar tratamento de erros para falhas de conexão;
- Coletar também links, datas e descrições das notícias;
- Criar uma interface simples para visualizar os dados coletados;
- Organizar os dados em uma tabela ou banco de dados.

## Autor

Projeto desenvolvido por Pedro como prática de web scraping com Python.
