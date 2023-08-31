# Web Scraping com Python

Este é um repositório que contém exemplos e informações relacionadas ao livro "Web Scraping com Python" de Ryan Mitchell. Neste repositório, você encontrará exemplos práticos e código relevante para entender e implementar técnicas de web scraping utilizando a linguagem de programação Python.

## Descrição

O livro "Web Scraping com Python" de Ryan Mitchell é uma referência valiosa para aqueles que desejam aprender a extrair informações da web de forma eficiente e eficaz. O livro aborda desde conceitos básicos até técnicas avançadas de web scraping, usando a linguagem Python como ferramenta principal.

Neste repositório, você encontrará exemplos e códigos relacionados a diferentes capítulos do livro. Os exemplos foram organizados de acordo com os tópicos abordados no livro, permitindo que você acompanhe e pratique os conceitos à medida que avança na leitura.

[Link para o PDF do livro](https://github.com/R1tzy/web-scraping-python/blob/main/livro/Web%20Scraping%20com%20Python%20-%202%C2%AA%20Edi%C3%A7%C3%A3o%20-%20Ryan%20Mitchell%20-%202019.pdf)

Obs. Alguns códigos de exemplos do livro não funciona, pois a estrutura dos sites testados foram modificadas. Os códigos de exemplo deste repositório está adaptando esses exemplos para que funcione de acordo com o conteúdo transmitido.

## Estrutura do Repositório

O repositório está organizado em pastas correspondentes aos diferentes capítulos do livro. Cada pasta contém exemplos de código e informações relevantes para o tópico abordado no respectivo capítulo. Abaixo está a estrutura geral do repositório:

## Parte I - Construindo Scrapers
### Capítulo 1 - Seu Primeiro Web Scraper
- Conectando-se a páginas web.
- Introdução ao BeautifulSoup e sua instalação.
- Executando o BeautifulSoup.
- Lidando com conexões confiáveis e tratando
   
### Capítulo 2 - Parsing de HTML Avançado
- Utilizando BeautifulSoup para analisar HTML.
- Explorando funcionalidades avançadas do BeautifulSoup.
- Utilização de `find()` e `find_all()` para navegar e extrair informações.
- Navegando em árvores HTML.
- Introdução a expressões regulares e sua combinação com BeautifulSoup.
- Acessando atributos e uso de expressões lambda.
   
### Capítulo 3 - Escrevendo Web Crawlers
- Criando web crawlers para percorrer domínios específicos.
- Rastreando um site completo.
- Coletando dados de um site inteiro.
- Rastreando pela internet e coletando informações.
   
### Capítulo 4 - Modelos de Web Crawling
- Planejamento e definição de objetos em web crawlers.
- Lidando com layouts de sites diversos.
- Estruturação de crawlers.
- Rastreamento baseado em pesquisa.
- Rastreamento por meio de links.
- Abordagem para rastrear diferentes tipos de páginas.
   
### Capítulo 5 - Scrapy
- Instalação e utilização da estrutura de web scraping Scrapy.
- Escrevendo um scraper simples.
- Spidering com regras.
- Criando e apresentando itens.
- Pipeline de itens e logging.
- Recursos adicionais fornecidos pelo Scrapy.
   
### Capítulo 6 - Armazenando Dados
- Gerenciamento de arquivos de mídia.
- Armazenamento de dados no formato CSV.
- Integração com o banco de dados MySQL.
- Exploração de técnicas de banco de dados e boas práticas.
- Uso do email para comunicação.

## Parte II - Coleta de Dados Avançada

### Capítulo 7 - Lendo Documentos
- Codificação de diferentes tipos de documentos.
- Manipulação de texto e codificação em uma escala global.
- Leitura de arquivos CSV.
- Trabalhando com PDFs.
- Lidando com documentos do Microsoft Word (.docx).
  
### Capítulo 8 - Limpando Dados Sujos
- Código para limpeza de dados coletados.
- Normalização de dados.
- Técnicas de limpeza após a coleta.
- Uso da ferramenta OpenRefine para refinamento dos dados.
  
### Capítulo 9 - Lendo e Escrevendo em Idiomas Naturais
- Resumindo dados coletados.
- Uso de modelos de Markov.
- Aplicação do conceito "Six Degrees of Wikipedia".
- Introdução ao Natural Language Toolkit (NLTK).
- Instalação, configuração e análise estatística com NLTK.
- Análise lexicográfica com NLTK.
- Exploração de recursos adicionais relacionados ao NLTK.

### Capítulo 10 - Rastreando Formulários e Logins
- Utilização da biblioteca Python Requests.
- Submissão de formulários básicos.
- Lidando com elementos como botões de rádio e caixas de seleção.
- Enviando arquivos e imagens por meio de formulários.
- Autenticação por meio de logins e cookies.
- Abordagem para lidar com problemas comuns em formulários.

### Capítulo 11 - Scraping de JavaScript
- Introdução rápida ao JavaScript.
- Uso de bibliotecas JavaScript comuns.
- Trabalhando com Ajax e HTML dinâmico.
- Executando JavaScript em Python com o Selenium.
- Utilização de webdrivers adicionais do Selenium.
- Lidando com redirecionamentos e considerações finais sobre JavaScript.

### Capítulo 12 - Rastreando por Meio de APIs
- Introdução às APIs (Interfaces de Programação de Aplicativos).
- Métodos HTTP e como trabalhar com APIs.
- Exploração de respostas de APIs.
- Parsing de JSON, um formato comum em APIs.
- Abordagem para lidar com APIs não documentadas.
- Encontrando, documentando e combinando APIs com outras fontes de dados.

### Capítulo 13 - Processamento de Imagens e Reconhecimento de Texto
- Visão geral de bibliotecas úteis.
- Uso da biblioteca Pillow.
- Aplicação do Tesseract para reconhecimento de texto em imagens.
- Exploração da biblioteca NumPy.
- Processamento de textos bem formatados.
- Realização de ajustes automáticos em imagens.
- Coleta de texto de imagens em sites.
- Treinamento do Tesseract para ler CAPTCHAs.

### Capítulo 14 - Evitando Armadilhas no Scraping
- Considerações éticas sobre o scraping.
- Técnicas para parecer um usuário humano.
- Ajuste de cabeçalhos em requisições.
- Lidando com cookies em JavaScript.
- Importância do timing.
- Recursos de segurança em formulários.
- Evitando armadilhas comuns.

### Capítulo 15 - Testando Seu Site com Scrapers
- Introdução aos testes.
- Compreensão dos testes de unidade.
- Uso do módulo unittest de Python.
- Testando a funcionalidade em um exemplo da Wikipédia.
- Comparação entre unittest e Selenium para testes.
  
### Capítulo 16 - Web Crawling em Paralelo
- Comparação entre processos e threads.
- Rastreamento de múltiplas threads.
- Lida com condições de concorrência e filas.
- Utilização do módulo threading.
- Rastreamento utilizando múltiplos processos.
- Demonstração de rastreamento da Wikipédia usando multiprocessamento.
- Comunicação entre processos e outra abordagem de multiprocessamento.
  
### Capítulo 17 - Fazendo Scraping Remotamente
- Vantagens do uso de servidores remotos.
- Estratégias para evitar bloqueio de endereços IP.
- Questões de portabilidade e extensibilidade.
- Exploração do uso do Tor e do PySocks.
- Hospedagem remota e considerações.
- Execução de scrapers em contas de hospedagem de sites.
- Execução de scrapers na nuvem e recursos adicionais.
  
### Capítulo 18 - Aspectos Legais e Éticos do Web Scraping
- Exploração de questões legais como marcas registradas, direitos autorais e patentes.
- Abordagem da lei de direitos autorais.
- Discussão sobre invasão de propriedade móvel.
- Abordagem da lei de Fraude e Abuso de Computadores.
- Considerações sobre o arquivo robots.txt e termos de serviço.
- Estudos de caso envolvendo disputas legais relacionadas ao scraping.
- Reflexões sobre ética e considerações finais.

## Como Usar Este Repositório

Cada pasta correspondente a um capítulo contém arquivos de código em Python, juntamente com qualquer outro recurso necessário, como arquivos de exemplo. Para acompanhar os exemplos do livro, você pode explorar as pastas de acordo com a ordem dos capítulos.

Sinta-se à vontade para clonar este repositório e explorar os exemplos para aprimorar sua compreensão e habilidades em web scraping com Python. Lembre-se de que o web scraping deve ser feito de maneira ética e respeitando os termos de uso dos sites que você está acessando.

## Aviso Legal

Este repositório destina-se apenas a fins educacionais e de aprendizado. Ao utilizar as técnicas de web scraping, certifique-se de cumprir todas as leis e regulamentos aplicáveis, além de respeitar os termos de uso dos sites que você está acessando.

**Aproveite sua jornada de aprendizado em web scraping com Python!**
