import requests

"""
Resolvendo formulários e logins usando o método post do request
"""
params = {'firstname':'Ryan', 'lastname':'Mitchell'}
r = requests.post('https://pythonscraping.com/pages/files/processing.php', data=params)
print(r.text)

