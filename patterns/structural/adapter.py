import smtplib

from email.mime.text import MIMEText


# This interface was implemented previously
class Mailer:

    @staticmethod
    def send(sender, recipients, subject, message):
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = recipients

        s = smtplib.SMTP('localhost')
        s.send_message(sender)
        s.quit()


# This is new interface which we want to serve together with the old one
class Logger:

    @staticmethod
    def output(message):
        print(message)


# This is the adapter to newly created interface
class LoggerAdapter:
    def __init__(self, what_i_have):
        self.what_i_have = what_i_have

    def send(self, sender, recipients, subject, message):
        log_message = "From: {}\nTo: {}\nSubject: {}\nMessage: {}".format(
            sender, recipients, subject, message
        )
        self.what_i_have.output(log_message)

    def __getattr__(self, item):
        return getattr(self.what_i_have, item)


if __name__ == '__main__':
    sender = LoggerAdapter(Logger)
    sender.send(
        'me@example.com',
        ['recipient1@example.com', 'recipien21@example.com'],
        'This is your message',
        'Have a good day'
    )