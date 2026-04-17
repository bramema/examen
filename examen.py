import csv
import json
from pathlib import Path

ruta = Path(_file_).parent
# ================= FUNCIONES =================

def guardar_csv(nombre_archivo, datos, campos):
    with open(ruta/nombre_archivo, mode="a", newline="") as archivo:
        writer = csv.DictWriter(archivo, fieldnames=campos)
        writer.writeheader()
        writer.writerows(datos)

def cargar_csv(nombre_archivo):
    try:
        with open(ruta/nombre_archivo, mode="r") as archivo:
            reader = csv.DictReader(archivo)
            return list(reader)
    except FileNotFoundError:
        return []

def facturar_con_descuento(nombre_archivo):
    try:
        with open(ruta/nombre_archivo, "w") as archivo:
            json.dump(factura, archivo, indent=4)
            print("Factura guardada en:", nombre_archivo)
    except:
        print("Error al guardar el archivo.")
                
    
    

# ================= LISTAS =================

datos_productos = cargar_csv("productos.csv")
datos_mesas = cargar_csv("mesas.csv")
datos_cliente = cargar_csv("clientes.csv")
datos_facturas_con_descuentos = cargar_csv("facturas.json")

# ================= MENU =================

while True:
    print("===========================================")
    print("=========== BIENVENIDO AL MENU ============")
    print("===========================================")
    print("1. productos")
    print("2. mesas")
    print("3. cliente")
    print("4. Facturacion")
    print("5. facturar con descuento")
    print("6. salir del menu")

    print("===========================================")
    op = input("opcion: ")
    print("===========================================")

    match op:
    
            # ===== PRODUCTOS =====
        case "1":
            print("1. Agregar producto")
            print("2. Ver productos")

            print("===========================================")
            producto = input("Opcion: ")
            print("===========================================")

            if producto == "1":
                diccionario = {
                    "codigo": input("Codigo: "),
                    "nombre": input("Nombre: "),
                    "valor": input("Valor: "),
                    "IVA": input("IVA: ")
                }
                datos_productos.append(diccionario)
                guardar_csv("productos.csv", datos_productos, ["codigo","nombre","valor","IVA"])
                print(" Producto guardado")

            elif producto == "2":
                print(" LISTA DE PRODUCTOS")
                for p in datos_productos:
                    print(p)

            else:
                print(" Opción no válida, intenta nuevamente")


        # ===== MESAS =====
        case "2":
            print("1. Agregar mesa")
            print("2. Ver mesas")

            print("===========================================")
            mesas = input("Opcion: ")
            print("===========================================")

            if mesas == "1":
                diccionario = {
                    "codigo": input("Codigo: "),
                    "nombre": input("Nombre: "),
                    "puesto": input("Puesto: ")
                }
                datos_mesas.append(diccionario)
                guardar_csv("mesas.csv", datos_mesas, ["codigo","nombre","puesto"])
                print("Mesa guardada")

            elif mesas == "2":
                print("LISTA DE MESAS")
                for m in datos_mesas:
                    print(m)
                    
            else:
                print(" Opción no válida, intenta nuevamente")

        # ===== CLIENTES =====
        case "3":
            print("1. Agregar cliente")
            print("2. Ver clientes")

            print("===========================================")
            cliente = input("Opcion: ")
            print("===========================================")

            if cliente == "1":
                diccionario = {
                    "identificación": input("ID: "),
                    "nombre": input("Nombre: "),
                    "teléfono": input("Teléfono: "),
                    "email": input("Email: ")
                }
                datos_cliente.append(diccionario)
                guardar_csv("clientes.csv", datos_cliente, ["identificación","nombre","teléfono","email"])
                print("Cliente guardado")

            elif cliente == "2":
                print(" LISTA DE CLIENTES")
                for c in datos_cliente:
                    print(c)

            else:
                print(" Opción no válida, intenta nuevamente")

        # ===== FACTURACION  =====

        case "4":
            print("====== FACTURACIÓN ======")

            if not datos_productos:
                print("No hay productos registrados")
                continue

            factura = []
            total = 0

            while True:
                codigo = input("Código del producto (o 0 para terminar): ")

                if codigo == "0":
                    break

                producto_encontrado = None
                for p in datos_productos:
                    if p["codigo"] == codigo:
                        producto_encontrado = p
                        break

                if producto_encontrado:
                    cantidad = int(input("Cantidad: "))
                    valor = float(producto_encontrado["valor"])
                    iva = float(producto_encontrado["IVA"])

                    subtotal = valor * cantidad
                    valor_iva = subtotal * (iva / 100)
                    total_producto = subtotal + valor_iva

                    factura.append({
                        "nombre": producto_encontrado["nombre"],
                        "cantidad": cantidad,
                        "subtotal": subtotal,
                        "iva": valor_iva,
                        "total": total_producto
                    })

                    total += total_producto

                else:
                    print("Producto no encontrado")

            print("======= FACTURA =======")
            for item in factura:
                print(item)

            print(f"TOTAL A PAGAR: {total}")

    # ===== FACTURACION CON DESCUENTO =====

        case "5":
            
                print("======== FACTURACIÓN CON DESCUENTO ========")
                print("===========================================")

                
                codigo_mesa = input("Ingrese código de mesa: ")
                cliente = input("Ingrese nombre del cliente: ")

                
                try:
                    total = float(input("Ingrese total de la cuenta: "))
                except:
                    print("Error: el total debe ser un número.")
                    

                
                aplicar_descuento = input("¿Aplica descuento? (si/no): ")

                descuento = 0

                if aplicar_descuento.lower() == "si":
                    try:
                        descuento = float(input("Ingrese porcentaje de descuento (0 a 50): "))
                    except:
                        print("Error: debe ingresar un número.")
                        
                    if descuento < 0 or descuento > 50:
                        print("Error: el descuento debe estar entre 0% y 50%.")
                        

                
                valor_descuento = total * (descuento / 100)
                total_final = total - valor_descuento

               
                print("===========================================")
                print("================ FACTURA ==================")
                print("===========================================")
                print("Cliente: ", cliente)
                print("Mesa: ", codigo_mesa)
                print("Total sin descuento: ", total)
                print("Descuento : ", descuento, "%")
                print("Total con descuento :", total_final)

                
                factura = {
                    "cliente": cliente,
                    "mesa": codigo_mesa,
                    "total_sin_descuento": total,
                    "porcentaje_descuento": descuento,
                    "valor_descuento": valor_descuento,
                    "total_con_descuento": total_final
                }

                
                nombre_archivo = "factura_" cliente

                

        case "6":
            print("Saliendo del sistema...")
            break

        case _:
            print("Opción inválida")       

    
