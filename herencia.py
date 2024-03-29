class Rectangulo:

    def __init__(self,base,altura) -> None:
        self.base = base
        self.altura = altura

    def area(self) -> int:
        return self.base * self.altura

class Cuadrado(Rectangulo):
    
    def __init__(self,lado) -> None:
        super().__init__(lado,lado)

if __name__ == '__main__':
    rectangulo = Rectangulo(base=3,altura=4)
    print(rectangulo.area())

    cuadrado = Cuadrado(lado=5)
    print(cuadrado.area())

        


