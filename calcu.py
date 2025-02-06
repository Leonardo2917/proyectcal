def calcular_pago_mensual(valor_principal, meses):
    interes_mensual = 1.87 / 100  # 1.87% convertido a decimal
    cuota_mensual = valor_principal / meses
    interes_total = valor_principal * interes_mensual
    pago_mensual = cuota_mensual + interes_total
    return pago_mensual, interes_total

# Solicitar al usuario el valor principal y los meses
valor_principal = float(input("Ingrese el valor principal: "))
meses = int(input("Ingrese la cantidad de meses: "))

# Calcular el pago mensual y el interés total
pago_mensual, interes_total = calcular_pago_mensual(valor_principal, meses)

# Mostrar resultados
print(f"Interés total mensual: {interes_total:.2f}")
print(f"Pago mensual total: {pago_mensual:.2f}")
