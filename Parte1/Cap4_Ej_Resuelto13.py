# Leer valor de la compra y color de la bolita
valor_compra=float(input("Ingrese el valor de la compra: "))
color_bolita=input("Color de la bolita (blanca, verde, amarilla, azul, roja): ").lower()

# Asignar porcentaje de descuento según el color
if color_bolita == "blanca":
    descuento=0
elif color_bolita == "verde":
    descuento=0.10
elif color_bolita == "amarilla":
    descuento=0.25
elif color_bolita == "azul":
    descuento=0.50
elif color_bolita == "roja":
    descuento=1.00

# Calcular valor final a pagar
valor_final=valor_compra * (1 - descuento)

# Mostrar resultado
print(f"Valor final a pagar: ${valor_final:.2f}")
