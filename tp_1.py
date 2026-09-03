"""
PROGRAMACIÓN 1 — LICENCIATURA EN SISTEMAS
Trabajo Práctico Nro. 1 — Sistema de gestión de ventas: Kiosco "El Campus"

Integrantes del grupo:
    - Becerra, Facundo Daniel
    - Vallejos, Carlos
"""

"""
Acá declaramos acumuladores, contadores y constantes para usar en 
el programa principal. Como no podemos usar tuplas o listas, decidimos 
ponerlas como variables globales. No es la mejor práctica, 
pero nos permite cumplir con las pautas que dieron.
"""
MONTO_MINIMO_DESCUENTO = 25000      # subtotal a partir del cual hay descuento
PORCENTAJE_DESCUENTO_MONTO = 10     # % de descuento por superar el monto
PORCENTAJE_DESCUENTO_EFECTIVO = 5   # % de descuento por pagar en efectivo
PORCENTAJE_RECARGO_CREDITO = 8      # % de recargo por pagar con crédito
total_recaudado = 0
cantidad_ventas = 0
venta_mas_alta = 0
total_golosinas = 0
total_bebidas = 0
total_almacen = 0
total_libreria = 0
cantidad_efectivo = 0
cantidad_debito = 0
cantidad_credito = 0

def pedir_entero_en_rango(mensaje, minimo, maximo):
    """Solicita al usuario un número entero dentro de un rango, reintentando
    hasta que la entrada sea correcta dentro de los límites establecidos.
    Recibe:  mensaje (str) a mostrar, minimo (int) y maximo (int) del rango.
    Devuelve: el número ingresado (int), garantizado dentro del rango.
    """
    entrada = input(mensaje)
    while not entrada.isdigit() or not (minimo <= int(entrada) <= maximo):
        print(f"Entrada inválida. Ingrese un número entero entre {minimo} y {maximo}.")
        entrada = input(mensaje)
    return int(entrada)

def pedir_real_en_rango(mensaje, minimo):
    """Solicita al usuario un número real estrictamente mayor que un mínimo,
    reintentando hasta que la entrada sea válida.
 
    Recibe:  mensaje (str) a mostrar, minimo (float) que el valor debe superar.
    Devuelve: el número ingresado (float), garantizado mayor que 'minimo'.
    """
    entrada = input(mensaje)
    while not entrada.replace('.', '', 1).isdigit() or not (minimo < float(entrada)):
        print(f"Entrada inválida. Ingrese un número real mayor que {minimo}.")
        entrada = input(mensaje)
    return float(entrada)

def nombre_de_categoría(categoria):
    """Sirve para pasar el número de categoría correspondiente
    a su denominación textual y evitar que escriba solo el número, que es
    menos legible y más difícil de asociar.
    Recibe: categoria (int) entre 1 y 4.
    Devuelve: el nombre de la categoría correspondiente como cadena.
    """
    match categoria:
        case 1:
            return "Golosinas"
        case 2:
            return "Bebidas"
        case 3:
            return "Comestibles"
        case 4:
            return "Librería"

def nombre_de_medio_de_pago(medio_de_pago):
    """Traduce el número del medio de pago correspondiente
    a su denominación textual; evita que escriba solo el número, que es
    menos legible y más difícil de asociar.
    Recibe: medio_de_pago (int) entre 1 y 3.
    Devuelve: el nombre del medio de pago correspondiente como cadena.
    """
    match medio_de_pago:
        case 1:
            return "Efectivo"
        case 2:
            return "Tarjeta de débito"
        case 3:
            return "Tarjeta de crédito"

def calcular_subtotal(precio_unitario, cantidad_unidades):
    """Calcula el subtotal de la venta.
    Recibe el precio unitario y la cantidad de unidades.
    Devuelve el subtotal.
    """
    return precio_unitario * cantidad_unidades

def calcular_descuento_por_monto(subtotal):
    """Calcula el descuento por superar el monto mínimo. Si no lo supera,
    el descuento es 0.
    Recibe: el subtotal de la venta.
    Devuelve: el descuento, que puede ser 0.
    """
    if subtotal > MONTO_MINIMO_DESCUENTO:
        return subtotal * PORCENTAJE_DESCUENTO_MONTO / 100
    return 0

def calcular_ajuste_medio_pago(subtotal, descuento_monto, medio_de_pago):
    """Calcula el ajuste según el medio de pago (descuento o recargo),
    ya sobre el importe con el descuento por monto aplicado.
    Recibe: subtotal, descuento_monto y medio_de_pago.
    Devuelve: el ajuste según corresponda.
    """
    importe_tras_descuento = subtotal - descuento_monto
    if medio_de_pago == 1: #O sea, para efectivo.   
        return (importe_tras_descuento * PORCENTAJE_DESCUENTO_EFECTIVO / 100)
    elif medio_de_pago == 3: #O sea, para crédito.    
        return importe_tras_descuento * PORCENTAJE_RECARGO_CREDITO / 100
    return 0 #Es el caso del débito, que no tiene ajuste ni recargo.

def calcular_importe_final(subtotal, descuento_monto, ajuste_medio_pago):
    """Calcula el importe final de la venta, combinando el subtotal,
    el descuento por monto y el ajuste por medio de pago.
    Recibe: subtotal, descuento_monto y ajuste_medio_pago.
    Devuelve: el importe final de la venta.
    """
    return subtotal - descuento_monto + ajuste_medio_pago

def categoria_producto():
    """Solicita al usuario la categoría del producto y devuelve el número
    correspondiente a la categoría elegida."""
    print("Seleccione la categoría del producto: ")
    print("1) Golosinas")
    print("2) Bebidas")
    print("3) Comestibles")
    print("4) Librería")
    categoria = pedir_entero_en_rango("Ingrese el número de la categoría: ", 1, 4)
    return categoria

def generar_ticket(categoria, subtotal, descuento_monto, ajuste_medio_pago, medio_de_pago, importe_final, codigo_suerte):
    """Muestra el ticket de la venta con el desglose completo. No calcula
    nada, solo imprime los valores que ya vienen calculados.
    """
    print("=== TICKET DE VENTA ===")
    print(f"Categoría del producto: {nombre_de_categoría(categoria)}")
    print(f"Subtotal: ${round(subtotal, 2)}")
    if descuento_monto > 0:
        print(f"Descuento por monto ({PORCENTAJE_DESCUENTO_MONTO}%): -${round(descuento_monto, 2)}")
    print(f"Medio de pago: {nombre_de_medio_de_pago(medio_de_pago)}")
    if ajuste_medio_pago < 0:
        print(f"Descuento por pago en efectivo ({PORCENTAJE_DESCUENTO_EFECTIVO}%): ${round(abs(ajuste_medio_pago), 2)}")
    elif ajuste_medio_pago > 0:
        print(f"Recargo por pago con crédito ({PORCENTAJE_RECARGO_CREDITO}%): +${round(ajuste_medio_pago, 2)}")
    print(f"IMPORTE FINAL: ${round(importe_final,2)}")
    print(f"Código de la suerte: ")
    print("========================")        

def calcular_promedio_venta(total_recaudado, cantidad_ventas):
    """Calcula el importe promedio por venta, sin dividir por cero
    si todavía no hay ventas.
    """
    if cantidad_ventas == 0:
        return 0
    return total_recaudado / cantidad_ventas

def determinar_medio_mas_utilizado(cant_efectivo, cant_debito, cant_credito):
    """Devuelve el nombre del medio de pago más utilizado en el día.
    """
    mayor = cant_efectivo
    nombre = "Efectivo"
    if cant_debito > mayor:
        mayor = cant_debito
        nombre = "Tarjeta de débito"
    if cant_credito > mayor:
        mayor = cant_credito
        nombre = "Tarjeta de crédito"
    return nombre

def mostrar_resumen_dia():
    """Muestra el resumen de ventas del día. No calcula nada directamente,
    usa calcular_promedio_venta y determinar_medio_mas_utilizado para eso.
    """
    print("\n=== RESUMEN DEL DÍA ===")
    if cantidad_ventas == 0:
        print("Todavía no se registraron ventas en el día.")
        return
    promedio = calcular_promedio_venta(total_recaudado, cantidad_ventas)
    medio_mas_usado = determinar_medio_mas_utilizado(cantidad_efectivo, cantidad_debito, cantidad_credito)
    print(f"Cantidad de ventas: {cantidad_ventas}")
    print(f"Total recaudado: ${round(total_recaudado, 2)}")
    print(f"Importe promedio por venta: ${round(promedio, 2)}")
    print(f"Venta más alta del día: ${round(venta_mas_alta, 2)}")
    print(f"Total en Golosinas: ${round(total_golosinas, 2)}")
    print(f"Total en Bebidas: ${round(total_bebidas, 2)}")
    print(f"Total en Comestibles: ${round(total_almacen, 2)}")
    print(f"Total en Librería: ${round(total_libreria, 2)}")
    print(f"Ventas en efectivo: {cantidad_efectivo}")
    print(f"Ventas con débito: {cantidad_debito}")
    print(f"Ventas con crédito: {cantidad_credito}")
    print(f"Medio de pago más utilizado: {medio_mas_usado}")

def mostrar_menu_principal():
    """Muestra las opciones del menú principal y devuelve la opción
    elegida por el usuario, ya validada.
    """
    print("\n=== KIOSCO EL CAMPUS ===")
    print("1) Registrar una venta.")
    print("2) Ver resumen del día.")
    print("3) Cerrar caja y salir.")
    opcion = pedir_entero_en_rango("Elija una opción: ", 1, 3)
    return opcion

# PROGRAMA PRINCIPAL
def menu():
    """Punto de entrada del programa: menú principal del kiosco."""
    opcion = 0
    while opcion != 3:
        opcion = mostrar_menu_principal()

        if opcion == 1:
            categoria = categoria_producto()
            precio_unitario = pedir_real_en_rango("Ingrese el precio unitario del producto: ", 0)
            cantidad_unidades = pedir_entero_en_rango("Ingrese la cantidad de unidades: ", 1, 9999)
            medio_de_pago = pedir_entero_en_rango("Ingrese el medio de pago (1: Efectivo, 2: Tarjeta de débito, 3: Tarjeta de crédito): ", 1, 3)
            subtotal = calcular_subtotal(precio_unitario, cantidad_unidades)
            descuento_monto = calcular_descuento_por_monto(subtotal)
            ajuste_medio_pago = calcular_ajuste_medio_pago(subtotal, descuento_monto, medio_de_pago)
            importe_final = calcular_importe_final(subtotal, descuento_monto, ajuste_medio_pago)
            #falta agregar la del código de la suerte - OPCIONAL
            generar_ticket(categoria, subtotal, descuento_monto, ajuste_medio_pago, medio_de_pago, importe_final) #AGREGAR CÓDIGO DE LA SUERTE - OPCIONAL
            #Actualizamos los acumuladores del día con lo de esta venta.
            total_recaudado = total_recaudado + importe_final
            cantidad_ventas = cantidad_ventas + 1
            if importe_final > venta_mas_alta:
                venta_mas_alta = importe_final
            if categoria == 1:
                total_golosinas = total_golosinas + importe_final
            elif categoria == 2:
                total_bebidas = total_bebidas + importe_final
            elif categoria == 3:
                total_almacen = total_almacen + importe_final
            else:
                total_libreria = total_libreria + importe_final
            if medio_de_pago == 1:
                cantidad_efectivo = cantidad_efectivo + 1
            elif medio_de_pago == 2:
                cantidad_debito = cantidad_debito + 1
            else:
                cantidad_credito = cantidad_credito + 1
        elif opcion == 2:
            mostrar_resumen_dia()
        else:
            print("Cerrando caja y saliendo del programa...")
    print("¡Hasta mañana, Don Ramón!")
menu()