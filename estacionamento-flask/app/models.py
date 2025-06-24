class Vaga:
    def __init__(self, numero, ocupada=False):
        self.numero = numero
        self.ocupada = ocupada

    def __repr__(self):
        return f'Vaga({self.numero}, ocupada={self.ocupada})'


class Estacionamento:
    def __init__(self, total_vagas=150):
        self.vagas = [Vaga(numero) for numero in range(1, total_vagas + 1)]

    def ocupar_vaga(self, numero):
        if 1 <= numero <= len(self.vagas):
            vaga = self.vagas[numero - 1]
            if not vaga.ocupada:
                vaga.ocupada = True
                return True
        return False

    def liberar_vaga(self, numero):
        if 1 <= numero <= len(self.vagas):
            vaga = self.vagas[numero - 1]
            if vaga.ocupada:
                vaga.ocupada = False
                return True
        return False

    def vagas_disponiveis(self):
        return [vaga for vaga in self.vagas if not vaga.ocupada]