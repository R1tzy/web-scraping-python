import requests
import pandas as pd

# Faz a solicitação HTTP para a página da Wikipédia e obtém a tabela
url = 'https://en.wikipedia.org/wiki/Comparison_of_text_editors'
tables = pd.read_html(url, header=1)

# Obtém a primeira tabela da página
df = tables[0]

# Remove colunas vazias e renomeia as colunas
df = df.dropna(axis=1, how='all')
df.columns = [
    'Name', 'Developer', 'Initial release', 'Latest release (Version, Date)',
    'Programming language', 'Cost (US$)', 'License', 'GUI', 'TUI or CLI'
]

# Salva os dados em um arquivo CSV
df.to_csv('editor.csv', index=False, encoding='utf-8')
