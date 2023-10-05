import smtplib
from email.mime.text import MIMEText

# Criando e enviando email python
msg = MIMEText('The body of the email is here')
msg['Subject'] = 'An Email Alert'
msg['From'] = 'fox_raposa64@hotmail.com'
msg['To'] = 'thiagolopesalmeida1230@gmail.com'

s = smtplib.SMTP(host='localhost', port=1025)
s.send_message(msg)
s.quit()

"""
Para funcionar isso é precioso ter um servidor 
SMTP local instalado ou definir um remoto,
eu utilizei o MailHog (https://github.com/mailhog/MailHog)
"""
