"""
PROGRAMACIÓN 1 — LICENCIATURA EN SISTEMAS
Trabajo Práctico Nro. 1 — Sistema de gestión de ventas: Kiosco "El Campus"

Integrantes del grupo:
    - 
    - 
"""

MONTO_MINIMO_DESCUENTO = 25000      # subtotal a partir del cual hay descuento
PORCENTAJE_DESCUENTO_MONTO = 10     # % de descuento por superar el monto
PORCENTAJE_DESCUENTO_EFECTIVO = 5   # % de descuento por pagar en efectivo
PORCENTAJE_RECARGO_CREDITO = 8      # % de recargo por pagar con crédito

def pedir_entero_en_rango(mensaje, minimo, maximo):

    entrada = input(mensaje)
    while not entrada.isdigit() or not (minimo <= int(entrada) <= maximo):
        print(f"Entrada inválida. Ingrese un número entero entre {minimo} y {maximo}.")
        entrada = input(mensaje)
    return int(entrada)

def pedir_real_en_rango(mensaje, minimo):
    entrada = input(mensaje)
    while not entrada.replace('.', '', 1).isdigit() or not (minimo <= float(entrada)):
        print(f"Entrada inválida. Ingrese un número real que sea como mínimo: {minimo}.")
        entrada = input(mensaje)
    return float(entrada)

def categoria_producto():
    print("Seleccione la categoría del producto:")
    print("1) Golosinas")
    print("2) Bebidas")
    print("3) Comestibles")
    print("4) Librería")
    categoria = pedir_entero_en_rango("Ingrese el número de la categoría: ", 1, 4)
    return categoria

def descuento_total(precio_unitario, cantidad_unidades, medio_de_pago):
    precio_por_cantidad = precio_unitario * cantidad_unidades
    if precio_por_cantidad > 25000:
          precio_por_cantidad = precio_por_cantidad * 0.90
    match medio_de_pago:
        case 1: 
              descuento = precio_por_cantidad * 0.95
        case 2:
              descuento = precio_por_cantidad
        case 3:
              descuento = precio_por_cantidad + (precio_por_cantidad * 0.92)
    return descuento

def generar_ticket(precio_unitario, categoria, cantidad_unidades, medio_de_pago, descuento):
    print("=== TICKET DE VENTA ===")
    print(f"Categoría del producto: {categoria}")
    print(f"Precio unitario: ${precio_unitario}")
    print(f"Cantidad de unidades: {cantidad_unidades}")
    match medio_de_pago:
        case 1:
            medio_de_pago = print("Efectivo")
        case 2:
            medio_de_pago = print("Debito")
        case 3:
            medio_de_pago = print("Credito")
    print(f"Medio de pago: {medio_de_pago}")
    print(f"Descuento aplicado: {round(descuento, 2)}")

    print("========================")

def prom(total_recaudado, cantidad_ventas):
    importe_promedio = total_recaudado / cantidad_ventas
    return importe_promedio

def menu():
    total_recaudado = 0
    cantidad_ventas = 0
    importe_promedio = 0
    venta_mas_alta = 0
    totales_por_categoria = 0
    contadores_por_medio_de_pago = 0
    
    opcion = 0
    while opcion != 3:
        print("\n=== KIOSCO EL CAMPUS ===")
        print("1) Registrar una venta.")
        print("2) Ver resumen del día.")
        print("3) Cerrar caja y salir.")
        opcion = pedir_entero_en_rango("Elija una opción: ", 1, 3)

        if opcion == 1:
            categoria = categoria_producto()
            precio_unitario = pedir_real_en_rango("Ingrese el precio unitario del producto: ", 0) #Revisar
            cantidad_unidades = pedir_entero_en_rango("Ingrese la cantidad de unidades: ", 1, 9999)
            medio_de_pago = pedir_entero_en_rango("Ingrese el medio de pago (1: Efectivo, 2: Tarjeta de débito, 3: Tarjeta de crédito): ", 1, 3)
            descuento = descuento_total(precio_unitario, cantidad_unidades, medio_de_pago)
            generar_ticket(precio_unitario, categoria, cantidad_unidades, medio_de_pago, descuento)
            if descuento != 0:
                cantidad_ventas += 1
                total_recaudado += descuento
                importe_promedio = prom(total_recaudado, cantidad_ventas)
                if descuento > venta_mas_alta:
                    venta_mas_alta = descuento
                match categoria:
                    case 1:
                        total_de_golosinas += descuento
                    case 2:
                        total_de_bebidas += descuento
                    case 3:
                        total_de_almacen += descuento
                    case 4:
                        total_de_libreria += descuento
                    match medio_de_pago:
                        case 1:
                            cont1 += 1
                        case 2:
                            cont2 += 1
                        case 3:
                            cont3 += 1
                    if cont1 > cont2 and cont2 > cont3:
            else:
                print("No se registro ninguna venta todavia")

            

        
        
        elif opcion == 2:
            
        else:
            
    print("¡Hasta mañana, Don Ramón!")
menu()