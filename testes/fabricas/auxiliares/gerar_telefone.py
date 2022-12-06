import random


class GerarTelefone:
    @staticmethod
    def gerar() -> str:
        formatos = ['(xx)xxxxx-xxxx', '(xx)xxxx-xxxx']
        formato = random.choice(formatos)
        numero = ''
        for char in formato:
            if char == 'x':
                numero += str(random.randint(0, 9))
            else:
                numero += char
        return numero
