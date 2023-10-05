import requests

"""
Nesse exemplos vamos fazer login 
e para isso precisamos lidar com 
os cookies, pois são eles que mantem 
nosso usuário logado no site
"""

params = {'username': 'teste', 'password': 'password'}
r = requests.post('https://pythonscraping.com'
                  '/pages/cookies/welcome.php', data=params)
print('Cookie está defindo como: ')
print(r.cookies.get_dict())
print('Indo para a página de perfil...')
r = requests.post('https://pythonscraping.com'
                  '/pages/cookies/profile.php', cookies=r.cookies)
print(r.text)

"""
Isso funciona bem em situações simples, 
mas e se estivéssemos lidando com um site 
mais complicado, que modificasse os cookies
com frequência,sem avisar, ou se preferíssemos, 
para começar, nem sequer pensar nos cookies? 
"""