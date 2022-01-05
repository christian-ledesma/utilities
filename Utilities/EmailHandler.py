import smtplib


class Gmail:
    def send(sender_login: dict, receiver, message, attachment=None):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_login["User"], sender_login["Password"])
        server.sendmail(sender_login["User"], receiver, message)
