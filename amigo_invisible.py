import argparse
import random
import re

import config
from amigo import amigo


class ErrorAmigoInvisible(Exception):
    pass


def compatibility(lista_amgs):
    for k in range(len(lista_amgs)):
        a = k % len(lista_amgs)
        b = (k + 1) % len(lista_amgs)

        amigo, recipient = lista_amgs[a].name, lista_amgs[b].name

        if amigo in config.ni_de_coña and \
                recipient in config.ni_de_coña[amigo]:
            return False

    return True


def send_letter(amigo, dry_run):
    mensaje = config.carta.get_email_message(amigo)

    with open(config.record, 'a') as f:
        f.write(mensaje)

    if dry_run:
        print(amigo)
    else:
        config.carta.send(amigo)

def set_recipients(amigos):

    for k in range(len(amigos) - 1):
        


def amigo_invisible(args):
    participantes = config.participantes

    check_emails(participantes)
    check_compatibility(participantes)
