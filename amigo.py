from functools import total_ordering


@total_ordering
class amigo(object):
    """
    Blueprint para el participante del amigo invisible.
    """
    def __init__(self, name, NIA):
        self.name = name
        self.NIA = NIA
        self.email = NIA + '@alumnos.uc3m.es'
        self.recipient = None

    def __eq__(self, other):
        return self.name.lower() == other.name.lower()

    def __lt__(self, other):
        assert isinstance(other, amigo)
        return self.name.lower() < other.name.lower()

    def __str__(self):
        if isinstance(self.recipient, amigo):
            return f'{self.name:12} -> {self.recipient.name}'

        return f'{self.name:12}'



