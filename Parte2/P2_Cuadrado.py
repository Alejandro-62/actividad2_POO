class Cuadrado:
    def __init__(self, lado):
        # Constructor para inicializar el lado del cuadrado
        self.lado = lado

    def calcular_area(self):
        # Calcula el área del cuadrado
        return self.lado * self.lado

    def calcular_perimetro(self):
        # Calcula el perímetro del cuadrado
        return 4 * self.lado

# Ejemplo de uso
cuadrado=Cuadrado(3)  # Crear un cuadrado con lado de longitud 3
print(f"Área del cuadrado: {cuadrado.calcular_area()}")  # Mostrar el área
print(f"Perímetro del cuadrado: {cuadrado.calcular_perimetro()}")  # Mostrar el perímetro