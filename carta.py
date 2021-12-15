import smtplib

import config
from amigo import amigo

class carta(object):
    """
    Define la carta que se enviara por email.
    """
    def __init__(self, from_name, from_mail, subject, body):
        self.from_name = from_name
        self.from_mail = from_mail
        self.subject = subject
        self.body = body

    def get_email_message(self, amigo):
        """
        Metodo que crea la carta pre.escriba en el config y asigna el nombre y
        recipiente.
        :param amigo: Objeto del participante.
        """
        message = \
            f'De: {self.from_name} <{self.from_mail}> \n'\
            f'Para: {amigo.name} <{amigo.email}>'\
            f'Asunto: {self.subject}\n\n'\
            f'{self.body}\n'

        message = message.replace('{amigo}', amigo.name)
        message = message.replace('{recipient}', amigo.recipient)

    def send(self, amigo):
        """
        Método que envía el correo al recipiente correspondiente.
        :param amigo:
        :return:
        """
        message_2_send = self.get_email_message(amigo)

        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(config.smtp_user, config.smtp_password)
            server.sendmail(self.from_mail, [amigo.email], message_2_send)

            print(f'Se mando la carta a {amigo.name}')

        except Exception as e:
            print(f'Error: failed to send message to: {e}')
