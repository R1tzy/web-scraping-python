import json
import requests

"""
Outra forma de obter dados de sites que 
utilizam javascrpit, sem precisar o selenium
para algo simples e por meio das APIs
"""

def getCountry(ipAddress):
    response = requests.get(f'https://ipinfo.io/{ipAddress}/json')
    
    if response.status_code == 200:
        responseJson = response.json()
        return responseJson['country']
    else:
        None

country = getCountry('50.78.253.58')

if country:
    print(f"{country}")
else:
    print('Error')
