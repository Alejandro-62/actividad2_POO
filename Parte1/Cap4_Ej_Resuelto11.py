# Leer tres números enteros
a=int(input("Ingrese el primer número: "))
b=int(input("Ingrese el segundo número: "))
c=int(input("Ingrese el tercer número: "))

# Determinar el mayor de los tres
if a > b and a > c:
    mayor=a
elif b > c:
    mayor=b
else:
    mayor=c

# Mostrar el mayor
print(f"El número mayor es: {mayor}")
