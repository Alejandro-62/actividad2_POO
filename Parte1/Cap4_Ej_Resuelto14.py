# Ingresar las ventas de los tres departamentos y el salario de los vendedores
VD1=float(input("Ingrese las ventas del departamento 1: "))
VD2=float(input("Ingrese las ventas del departamento 2: "))
VD3=float(input("Ingrese las ventas del departamento 3: "))
SALAR=float(input("Ingrese el salario de los vendedores en cada departamento: "))

# Calcular el total de ventas
TOTVEN=VD1+VD2+VD3

# Calcular el porcentaje equivalente al 33% de las ventas totales
PORVEN=0.33*TOTVEN

# Calcular el salario de los vendedores en cada departamento
if VD1>PORVEN:
    SALAR1=SALAR+0.2*SALAR  # Si las ventas del depto. 
    #1 son mayores que el 33%, se aumenta el 20% al salario
else:
    SALAR1=SALAR

if VD2>PORVEN:
    SALAR2=SALAR+0.2*SALAR  # Lo mismo para el depto. 2
else:
    SALAR2=SALAR

if VD3>PORVEN:
    SALAR3=SALAR+0.2*SALAR  # Lo mismo para el depto. 3
else:
    SALAR3=SALAR

# Imprimir los salarios finales
print(f"SALARIO VENDEDORES DEPTO. 1: {SALAR1}")
print(f"SALARIO VENDEDORES DEPTO. 2: {SALAR2}")
print(f"SALARIO VENDEDORES DEPTO. 3: {SALAR3}")
