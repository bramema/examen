import json
import os
def ranking_productos_menos_vendidos(fecha_inicio, fecha_fin, facturas):
    productos = {}

    for factura in facturas :
        if fecha_inicio <= factura["fecha"] <= fecha_fin:
            for item in factura ["item"]:
                nombre = item ["producto"]
                cantidad = item ["cantidad"]

                if nombre in productos:
                    productos[nombre] = cantidad
                else:
                    productos[nombre] = cantidad

    menos = list(productos.items())

    
    
