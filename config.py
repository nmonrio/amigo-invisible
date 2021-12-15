from carta import carta
from amigo import amigo

# Email para mandar a quien te ha tocado
smtp_user = 'amigo.invisible.gif.giti@gmail.com'
smtp_password = 'Tuputamadreenpijama2021'

# Editar el body para
cartita = carta(
    from_name = 'Amigo Invisible',
    from_mail = smtp_user,
    subject = '[GIF] Amigo Invisible 2021 #NO-SPAM',
    body = """
    Buenas {amigo}!!\n\n
    
    De parte de los delegados invisibles, aquí tienes a tu amigo invisible:\n 
    {recipient}. \n\n
    Cositas importantes: \n
    1. La entrega se hará la tarde del último examen final, es decir 21/01/22. \n
    2. El importe máximo son 10€. Eso no quitas que puedan ser artesanales o straight-up bullshit. \n
    3. Feliz Navidad y ojala te toque algo muuu chulo!! \n\n
    
    Besetes, \n\n
    
    Papá y Mamá Noel
    
    """
)

participantes = [
    # Escribir cada participante junto a su NIA tal que:
    # amigo('Nombre'. '100XXXXXX')
    amigo('Nerea M', '100452085'),
    amigo('Irene P', '100452087'),
    amigo('Irene R', '100454404'),
    amigo('Cockito', '100454279')
]

ni_de_coña = {
    # Gente que ni de coña les toque juntos por el bien de la clase
    # 'Pª que regala' : 'Pª que recibe'
    'Cockito' : ('Nerea M',),  # Que cockito no le regale a Nere
}

# Archivo con las asignaciones.
record = 'amigo_invisible_emails.txt'