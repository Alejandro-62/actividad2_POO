# Nombre del empleado
Nombre=input("Introduce el nombre del empleado: ")

# Salario básico por hora
SalarioHora=float(input("Introduce el salario básico por hora: "))

# Número de horas trabajadas en el mes
HorasTrabajadas=int(input("Introduce el número de horas trabajadas en el mes: "))

# Salario mensual
SalarioMensual=SalarioHora * HorasTrabajadas

# Verificar si el salario es mayor a $450.000
if SalarioMensual > 450000:
    # Mostrar el nombre y el salario mensual
    print(f"Empleado: {Nombre}")
    print(f"Salario mensual: ${SalarioMensual:,.2f}")
else:
    # Mostrar sólo el nombre del empleado
    print(f"Empleado: {Nombre}")