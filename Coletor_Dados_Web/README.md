# Coletor de Dados Web com Python

Este projeto é um exemplo simples de coleta de dados na web utilizando Python. A aplicação acessa a página inicial do portal G1, identifica os links das notícias disponíveis e exibe os títulos encontrados diretamente no terminal.

## Objetivo do Projeto

O objetivo deste projeto é praticar conceitos básicos de web scraping com Python, utilizando bibliotecas externas para realizar requisições HTTP e analisar o conteúdo HTML de uma página. Neste caso, o sistema acessa um site de notícias e coleta automaticamente os títulos das matérias disponíveis.

## Funcionalidades

- Acesso automático a uma página da web;
- Realização de requisição HTTP para obter o conteúdo do site;
- Leitura e interpretação do código HTML da página;
- Busca por links de notícias com uma classe HTML específica;
- Exibição dos títulos das notícias no terminal;
- Numeração automática das notícias coletadas.

## Tecnologias Utilizadas

- Python
- Biblioteca `requests`
- Biblioteca `BeautifulSoup`
- HTML
- Web Scraping

## Como Funciona

O programa define a URL da página inicial do G1 e utiliza a biblioteca `requests` para realizar uma requisição ao site. Após receber o conteúdo da página, o HTML é processado pela biblioteca `BeautifulSoup`, que permite localizar elementos específicos dentro da estrutura do site.

Depois disso, o código procura todos os elementos `<a>` que possuem a classe `feed-post-link`, utilizada para identificar links de notícias na página. Em seguida, cada notícia encontrada é exibida no terminal de forma numerada, mostrando apenas o texto do título.

## Requisitos e Como Rodar o Código

Para executar este projeto, é necessário ter o Python instalado no computador e estar conectado à internet, pois a aplicação acessa uma página web em tempo real.

Primeiro, instale as bibliotecas necessárias com o comando abaixo:

```bash
pip install requests beautifulsoup4
```

Depois, abra o arquivo do projeto em uma IDE ou editor de código, como VS Code, PyCharm ou outro de sua preferência.

Em seguida, execute o arquivo Python pelo terminal com o comando:

```bash
python nome_do_arquivo.py
```

Ao executar o programa, ele acessará o site definido no código, coletará os títulos das notícias encontradas e exibirá os resultados diretamente no terminal.

## Possíveis Melhorias Futuras

- Permitir que o usuário informe a URL desejada;
- Salvar os dados coletados em um arquivo `.txt` ou `.csv`;
- Coletar também os links das notícias;
- Coletar datas, categorias e descrições das matérias;
- Adicionar tratamento de erros para falhas de conexão;
- Criar uma interface simples para visualizar as notícias coletadas;
- Organizar os dados coletados em uma tabela ou banco de dados.

## Autor

Projeto desenvolvido por Pedro como prática de web scraping com Python.
