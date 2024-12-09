import math

# Solicitar el valor del lado del triángulo
lado=float(input("Ingrese el valor del lado del triángulo en metros: "))

# Calcular el perímetro, altura y área
perimetro=lado*3
altura=(lado*math.sqrt(3))/2
area=(lado*altura)/2

# Mostrar los resultados
print(f"El perímetro es de {perimetro} metros")
print(f"La altura es de {altura} metros")
print(f"El área es de {area} metros cuadrados")
