import smtplib, ssl

port = "465"
smtp_server = "smtp.gmail.com"
sender_email = ""
receiver_email = "melvin.magnehag@elev.ga.ntig.se"
password = ""
message = """\
Subject: Gay midget porn

i love midget porn so much
"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)