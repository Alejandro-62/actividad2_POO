# Peso de las esferas A, B y C
PesoA=float(input("Ingrese el peso de la esfera A: "))
PesoB=float(input("Ingrese el peso de la esfera B: "))
PesoC=float(input("Ingrese el peso de la esfera C: "))

# Comparar los pesos para determinar cuál es la esfera más pesada
if PesoA > PesoB and PesoA > PesoC:
    print("La esfera A tiene el mayor peso.")
elif PesoB > PesoA and PesoB > PesoC:
    print("La esfera B tiene el mayor peso.")
elif PesoC > PesoA and PesoC > PesoB:
    print("La esfera C tiene el mayor peso.")
else:
    print("Dos o más esferas tienen el mismo peso máximo.")