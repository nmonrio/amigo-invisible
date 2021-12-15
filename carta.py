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

    def send(self, amigo):
