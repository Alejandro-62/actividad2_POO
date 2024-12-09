class Rectangulo:
    def __init__(self, base, altura):
        # Constructor para inicializar la base y la altura del rectángulo
        self.base = base
        self.altura = altura

    def calcular_area(self):
        # Calcula el área del rectángulo
        return self.base * self.altura

    def calcular_perimetro(self):
        # Calcula el perímetro del rectángulo
        return 2 * self.base + 2 * self.altura

# Ejemplo de uso
rectangulo = Rectangulo(10, 5)  # Crear un rectángulo con base 10 y altura 5
print(f"Área del rectángulo: {rectangulo.calcular_area()}")  # Mostrar el área
print(f"Perímetro del rectángulo: {rectangulo.calcular_perimetro()}")  # Mostrar el perímetro
