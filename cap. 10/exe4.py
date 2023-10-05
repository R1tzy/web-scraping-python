import requests

"""
Para resolver a sistuação do exe3.py, 
podemos usar a função session disponível 
no requests
"""

session = requests.Session()

params = {'username': 'teste', 'password': 'password'}
s = session.post('https://pythonscraping.com/pages/cookies/welcome.php', params=params)
print('Cookie está defindo como: ')
print(s.cookies.get_dict())
print('Indo para a página de perfil...')
s = session.post('https://pythonscraping.com/pages/cookies/profile.php')
print(s.text)

"""
Nesse exemplo, o objeto sessão (obtido 
por meio requests.Session()) mantém o 
controle das informações da sessão, por
exemplo, cookies, cabeçalhos e até mesmo 
informações sobre os protocolos que podem 
executar sobre o HTTP, como o HTTPAdapters.

Você deve ter notado que quando usa s.cookies.get_dict() 
ele resulta em {} e quando usa r.cookies.get_dict() 
resulta em {'loggedin': '1', 'username': 'teste'}, 
isso ocorre porque a sessão gerencia os cookies 
automaticamente para você, enquanto em solicitações 
individuais, você deve gerenciar os cookies manualmente.
"""