# Leer datos del trabajador
nombres=input("Nombres: ")
horas_trabajadas=int(input("Horas trabajadas: "))
valor_hora=float(input("Valor por hora: "))

# Calcular salario base
salario=valor_hora * min(horas_trabajadas, 40)

# Calcular pago de horas extras
if horas_trabajadas > 40:
    extras=horas_trabajadas - 40
    if extras <= 8:
        salario += extras * valor_hora * 2
    else:
        salario += 8 * valor_hora * 2 + (extras - 8) * valor_hora * 3

# Mostrar resultado
print(f"Nombres: {nombres}")
print(f"Salario semanal: ${salario:.2f}")
