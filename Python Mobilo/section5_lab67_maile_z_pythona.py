import smtplib

mailFrom = "Tinka@wp.pl"
mailTo = ["krystyna.m.piatkowska@gmail.com", "mamasz.tina@gmail.com"]
mailSubject = 'Pozdrowionka'
mailBody = '''
bez polskich liter
Tinka'''

message = '''From:{}
Subject:{}
{}
'''.format(mailFrom, mailSubject, mailBody)

user = 'mamasz.tina@gmail.com'
password = ''


server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(user, password)
server.sendmail(user, mailTo, message)
server.close()
print('mail sent')

