import requests
from bs4 import BeautifulSoup
import csv

html = requests.get('https://en.wikipedia.org/wiki/Comparison_of_text_editors')

bs = BeautifulSoup(html.content, 'html.parser')
# A tabela principal de comparação é atualmente a primeira tabela da página
table = bs.find_all('table', {'class': 'wikitable'})[0]
tbody = table.find('tbody')
rows = tbody.find_all('tr')

# Defina manualmente os nomes das colunas
column_headers = [
    'Name', 'Developer', 'Initial release', 'Latest release (Version, Date)',
    'Programming language', 'Cost (US$)', 'License', 'GUI', 'TUI or CLI'
]

# Remova espaços ou substitua por sublinhados no nome do arquivo CSV
csvFile = open('cap. 6/editors.csv', 'wt+', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
try:
    writer.writerow(column_headers)
    # Pule as duas primeiras linhas que contêm cabeçalhos HTML
    for row in rows[2:]:
        """
        Esse pulo de linha é por que no site está confuso na hora que
        faz o web scraping, é por esse mesmo motivo que defini manualmente
        as colunas
        """
        csvRow = []
        cells = row.find_all(['td', 'th'])
        values = []

        """
        O GUI e CLI foi preciso fazer esse lógica, por causa
        que na tabela é usado imagens ✔️ e ❌, então useo o
        data-sort-value para saber se é yes ou no
        """
        for cell in cells:
            if cell.has_attr('data-sort-value'):
                values.append(cell['data-sort-value'])

            csvRow.append(cell.get_text(strip=True))

        gui = ''
        cli = ''

        if len(values) == 2:
            gui, cli = values
        elif len(values) == 1:
            gui = values[0]

        if 'Latest release (Version, Date)' in column_headers \
                and len(csvRow) >= 4:
            latest_release_index = column_headers.index(
                'Latest release (Version, Date)'
            )
            td3 = csvRow.pop(3) if len(csvRow) > 3 else ''
            td4 = csvRow.pop(3) if len(csvRow) > 3 else ''
            csvRow.insert(latest_release_index, f'{td3} {td4}')
        csvRow.insert(column_headers.index('GUI'), gui)
        csvRow.insert(column_headers.index('TUI or CLI'), cli)

        writer.writerow(csvRow)
finally:
    csvFile.close()

"""
Nesse exemplos vamos pegar a tabela do artigo Comparação
entre editores de texto, https://en.wikipedia.org/wiki/
Comparison_of_text_editors da Wikipédia. Fazer um
tratamento dos dados e salvar um arquivo csv.
"""
