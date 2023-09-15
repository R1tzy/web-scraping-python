import pymysql

# EXEMPLO DE USO DO MYSQL NO PYTHON

# Faz a conexão com o banco de dados
conn = pymysql.connect(host='127.0.0.1', user='root',
                       passwd='', db='mysql', port=3306)

# Cria o cursor
cur = conn.cursor() 
# Executa o cursor usando o database scraping
cur.execute('USE scraping')
# Executa o cursor selecionando tudo da tabela pages onde id = 3
cur.execute('SELECT * FROM pages WHERE id=3')
# Printa o cursor do resultado da consulta
print(cur.fetchone())
# Fecha o cursor
cur.close()
# Fecha a conexão
conn.close()