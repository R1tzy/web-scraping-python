import re
#Use regex para validar email
emails = [
    'exemplo@email.com',
    'usuario123@email.net',
    'teste.teste@email.org',
    'exemplo@.com',
    'usuario123@.net'
]

# posso fazer o pattern assim ou usar re.compile() caso vai usar várias vezes (desempenho)
pattern_email = r'[A-Za-z0-9\._+]+@+[A-Za-z]+\.(com|org|edu|net)'
for email in emails:
    if re.search(pattern_email, email):
        print(f'{email} é válido')
    else:
        print(f'{email} é inválido')

telefones = [
    '(11) 1234-5678',
    '(21) 98765-4321',
    '(85) 2345-6789',
    '(313) 587654-3210',
]
pattern_telefone = '\([0-9]{2}\) [0-9]{4,5}-[0-9]{4}'

for telefone in telefones:
    if re.search(pattern_telefone, telefone):
        print(f'{telefone} é válido')
    else:
        print(f'{telefone} é inválido')
