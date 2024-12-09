# Solicitar nombre del empleado
nombre=input("Ingrese el nombre del empleado: ")

# Solicitar código del empleado
codigoE=int(input("Ingrese el código del empleado: "))

# Solicitar las horas trabajadas
horastraba=float(input("Ingrese las horas trabajadas en el mes: "))

# Solicitar el valor por hora
valorhora=float(input("Ingrese valor de la hora: "))

# Solicitar el porcentaje de retención de fuente
retefuentes=float(input("Ingrese porcentaje de retención de fuente: "))

# Calcular salario bruto
salariobruto=horastraba*valorhora

# Calcular la retención de fuente
retiene=(retefuentes*salariobruto)/100

# Calcular salario neto
salarioneto=salariobruto-retiene

# Imprimir los resultados
print(f"El empleado {nombre} con código {codigoE} trabajó {horastraba} horas.")
print(f"Tiene un salario bruto de: {salariobruto} y su salario neto es: {salarioneto}")
