# Leer datos del estudiante
num_inscripcion=input("Número de inscripción: ")
nombres=input("Nombres: ")
patrimonio=float(input("Patrimonio: "))
estrato=int(input("Estrato social: "))

# Calcular el pago base
pago_matricula=50000

# Aplicar incremento si cumple condiciones
if patrimonio > 2000000 and estrato > 3:
    pago_matricula += patrimonio * 0.03

# Mostrar resultados
print(f"Número de inscripción: {num_inscripcion}")
print(f"Nombres: {nombres}")
print(f"Pago de matrícula: ${pago_matricula:.2f}")
