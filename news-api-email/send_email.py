import smtplib, ssl


def send_email(message):
    print("✅ send_email called with message:")
    print(message)
    host = "smtp.gmail.com"
    port = 465

    username = 'xx@gmail.com'
    password = 'sfdsfdsfdsf'

    receiver = 'xx@gmail.com'
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)