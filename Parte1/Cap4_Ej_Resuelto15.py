# Leer los pesos de las esferas
A=float(input("Peso de la esfera A: "))
B=float(input("Peso de la esfera B: "))
C=float(input("Peso de la esfera C: "))
D=float(input("Peso de la esfera D: "))

# Comparar los pesos para encontrar la diferente
if A == B == C:  # Caso: A, B y C tienen el mismo peso
    diferente="D"
    diferencia="mayor" if D > A else "menor"
elif A == B == D:  # Caso: A, B y D tienen el mismo peso
    diferente="C"
    diferencia="mayor" if C > A else "menor"
elif A == C == D:  # Caso: A, C y D tienen el mismo peso
    diferente = "B"
    diferencia="mayor" if B > A else "menor"
else:  # Caso: B, C y D tienen el mismo peso
    diferente = "A"
    diferencia = "mayor" if A > B else "menor"

# Mostrar resultados
print(f"La esfera diferente es {diferente} y es de {diferencia} peso.")
