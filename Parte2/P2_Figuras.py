import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio


class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        return self.largo * self.ancho

    def calcular_perimetro(self):
        return 2 * (self.largo + self.ancho)


class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

    def calcular_perimetro(self):
        return 4 * self.lado


class TrianguloRectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

    def calcular_perimetro(self):
        hipotenusa = math.sqrt(self.base ** 2 + self.altura ** 2)
        return self.base + self.altura + hipotenusa

    def determinar_tipo_triangulo(self):
        if self.base == self.altura:
            print("El triángulo es isósceles.")
        elif self.base ** 2 + self.altura ** 2 == (math.sqrt(self.base ** 2 + self.altura ** 2)) ** 2:
            print("El triángulo es rectángulo.")
        else:
            print("El triángulo es escaleno.")


# Código principal
if __name__ == "__main__":
    figura1 = Circulo(2)
    figura2 = Rectangulo(1, 2)
    figura3 = Cuadrado(3)
    figura4 = TrianguloRectangulo(3, 5)

    print(f"El área del círculo es = {figura1.calcular_area():.2f}")
    print(f"El perímetro del círculo es = {figura1.calcular_perimetro():.2f}")
    print()
    print(f"El área del rectángulo es = {figura2.calcular_area():.2f}")
    print(f"El perímetro del rectángulo es = {figura2.calcular_perimetro():.2f}")
    print()
    print(f"El área del cuadrado es = {figura3.calcular_area():.2f}")
    print(f"El perímetro del cuadrado es = {figura3.calcular_perimetro():.2f}")
    print()
    print(f"El área del triángulo es = {figura4.calcular_area():.2f}")
    print(f"El perímetro del triángulo es = {figura4.calcular_perimetro():.2f}")
    figura4.determinar_tipo_triangulo()
