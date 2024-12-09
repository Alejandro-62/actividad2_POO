import math

# Solicitar los valores de los lados del triángulo
a=float(input("Ingrese el valor del primer lado del triángulo en metros: "))
b=float(input("Ingrese el valor del segundo lado del triángulo en metros: "))
c=float(input("Ingrese el valor del tercer lado del triángulo en metros: "))

# Calcular el perímetro y semiperímetro
perimetro=a+b+c
semiperimetro=perimetro/22

# Calcular el área usando la fórmula de Herón
area=math.sqrt(semiperimetro*(semiperimetro-a)*(semiperimetro-b)*(semiperimetro-c))

# Mostrar los resultados
print(f"El perímetro es de {perimetro} metros")
print(f"El semiperímetro es de {semiperimetro} metros")
print(f"El área es de {area} metros cuadrados")
