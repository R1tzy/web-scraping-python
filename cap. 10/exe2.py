import requests


# Maneira de enviar imagem em um formulário
files = {'uploadFile': open('img/img01.jpg', 'rb')}
r = requests.post('https://www.pythonscraping.com/'
                  'pages/files/processing2.php', files=files)
print(r.text)

