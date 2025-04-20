
def calcular_ganancia(precio_unitario, precio_venta, porcentaje):
    try:
        precio_unitario = float(precio_unitario)
        precio_venta = float(precio_venta)
        porcentaje = float(porcentaje)
        return round(precio_venta - (precio_unitario + (porcentaje / 100) * precio_venta), 2)
    except Exception as e:
        return 0.0
