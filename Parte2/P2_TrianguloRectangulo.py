import math

class TrianguloRectangulo:
    def __init__(self, base, altura):
        # Constructor para inicializar la base y la altura
        self.base = base
        self.altura = altura

    def calcular_area(self):
        # Calcula el área del triángulo rectángulo
        return (self.base * self.altura) / 2

    def calcular_hipotenusa(self):
        # Calcula la hipotenusa usando el teorema de Pitágoras
        return math.sqrt(self.base**2 + self.altura**2)

    def calcular_perimetro(self):
        # Calcula el perímetro del triángulo rectángulo
        return self.base + self.altura + self.calcular_hipotenusa()

    def determinar_tipo_triangulo(self):
        # Determina el tipo del triángulo
        hipotenusa = self.calcular_hipotenusa()
        if self.base == self.altura == hipotenusa:
            print("Es un triángulo equilátero")
        elif self.base != self.altura and self.base != hipotenusa and self.altura != hipotenusa:
            print("Es un triángulo escaleno")
        else:
            print("Es un triángulo isósceles")

# Ejemplo de uso
triangulo = TrianguloRectangulo(3, 4)
print(f"Área del triángulo: {triangulo.calcular_area()}")
print(f"Hipotenusa del triángulo: {triangulo.calcular_hipotenusa()}")
print(f"Perímetro del triángulo: {triangulo.calcular_perimetro()}")
triangulo.determinar_tipo_triangulo()
