import math

class Circulo:
    def __init__(self, radio):
        # Constructor para inicializar el radio del círculo
        self.radio = radio

    def calcular_area(self):
        # Calcula el área del círculo
        return math.pi * (self.radio ** 2)

    def calcular_perimetro(self):
        # Calcula el perímetro del círculo
        return 2 * math.pi * self.radio

# Ejemplo de uso
circulo=Circulo(5)  # Crear un círculo con radio 5
print(f"Área del círculo: {circulo.calcular_area()}")  # Mostrar el área
print(f"Perímetro del círculo: {circulo.calcular_perimetro()}")  # Mostrar el perímetro
