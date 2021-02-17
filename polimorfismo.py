class Persona:

    def __init__(self,nombre) -> None:
        self.nombre = nombre

    def avanza(self):
        print(f'ando caminando me llamo {self.nombre}')



class Ciclista(Persona):

    def __init__(self, nombre) -> None:
        super().__init__(nombre)

    def avanza(self):
        print(f'Ando moviendome en bicicleta me llamo {self.nombre}')


def main():
    persona1 = Persona('Frank')
    persona1.avanza()
    persona2 = Ciclista('Pedrito')
    persona2.avanza()




if __name__ == '__main__':
    main()            
