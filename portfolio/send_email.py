import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = 'email@gmail.com'
password = 'password'

receiver = 'emailreceiver@gmail.com'
context = ssl.create_default_context()

message = """
HI!
How are you
Bye!
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)