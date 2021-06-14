import smtplib, ssl

def send_email_alert(subject, bodytext):
    smtp_server = "smtp.gmail.com"
    sender_email = "plidev86@gmail.com"
    password = ""
    receiver_email = "paul.j.li.97@gmail.com"  # Enter receiver address
    message = """\
    Paul's Alerter: {}

    {}""".format(subject, bodytext)


    # Create a secure SSL context
    # context = ssl.create_default_context()
    context = ssl.SSLContext(ssl.PROTOCOL_TLS)

    server = smtplib.SMTP(smtp_server, 587)
    #server.ehlo()
    server.starttls(context=context)
    #server.ehlo()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)

    server.quit()