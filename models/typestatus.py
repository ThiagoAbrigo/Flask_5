from enum import Enum 

class TypeStatus(Enum):
    SOLTERO = 'Soltero'
    CASADO = 'Casado'
    DIVORCIADO = 'Divorciado'
    VIUDO = 'Viudo'
    @staticmethod
    def choices():
        return [(estado.name, estado.value) for estado in TypeStatus]