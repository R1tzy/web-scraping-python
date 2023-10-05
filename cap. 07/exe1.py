import requests

"""
Para sites(antigos ou mais simples) com codificação em
formato de texto. A maioria dos navegadores não terá
problemas para exibir esses arquivostexto, e você poderá
coletar seus dados sem grandes dificuldades.

Desvantagem - não podermos usar tags HTML para saber
onde estão os textos que realmente queremos e excluir
os textos indesejados.
"""
textPage = requests.get('https://www.pythonscraping.com/'
                        'pages/warandpeace/chapter1.txt')
if textPage.status_code == 200:
    print(textPage.text)
else:
    print('Falha ao carregar o conteúdo. '
          'Código de status:', textPage.status_code)
