import requests
from requests.auth import HTTPBasicAuth

"""
Antes do surgimento dos cookies, 
um modo conhecido de lidar com logins
era com a autenticação de acesso básica
do HTTP
"""

auth = HTTPBasicAuth('teste', 'password')
r = requests.post(url='https://pythonscraping.com'
                  '/pages/auth/login.php', auth=auth)
print(r.text)

"""
Embora essa pareça uma requisição 
POST comum, um objeto HTTPBasicAuth 
é passado como o argumento auth na 
requisição. O texto resultante será 
a página protegida pelo nome do usuário 
e a senha (ou uma página Access Denied 
[Acesso negado], caso a requisição falhe).
"""