class Lavadora:

    def __init__(self) -> None:
        pass

    def lavar(self, temperatura='caliente'):
        self._llenar_tanque_de_agua(temperatura)
        self._añadir_jabon()
        self._lavar()
        self._centrifugar()

    def _llenar_tanque_de_agua(self,temperatura):
        print(f'estamos llenando el tanque con agua {temperatura}')

    def _añadir_jabon(self):
        print(f'añadiendo jabon')

    def _lavar(self):
        print(f'lavando...')

    def _centrifugar(self):
        print(f'centrifugando...')                


if __name__ == '__main__':
    lavadora = Lavadora()
    lavadora.lavar()