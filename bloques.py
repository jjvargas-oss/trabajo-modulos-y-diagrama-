def leer_cliente():
    nombre = input("Nombre del cliente: ")
    return nombre


def calcular_subtotal(precio1, cantidad1, precio2, cantidad2):
    subtotal1 = precio1 * cantidad1
    subtotal2 = precio2 * cantidad2

    return subtotal1, subtotal2


def calcular_descuento(
    subtotal1, porcentaje1, subtotal2, porcentaje2
):
    descuento1 = subtotal1 * porcentaje1 / 100
    descuento2 = subtotal2 * porcentaje2 / 100

    return descuento1, descuento2


def calcular_total_productos(total1, total2):
    total_compra = total1 + total2
    return total_compra


def calcular_total(
    precio1, cantidad1, porcentaje1, impuesto1,
    precio2, cantidad2, porcentaje2, impuesto2
):
    subtotal1, subtotal2 = calcular_subtotal(
        precio1, cantidad1, precio2, cantidad2
    )

    descuento1, descuento2 = calcular_descuento(
        subtotal1, porcentaje1, subtotal2, porcentaje2
    )

    iva1 = (subtotal1 - descuento1) * impuesto1 / 100
    iva2 = (subtotal2 - descuento2) * impuesto2 / 100

    total1 = subtotal1 - descuento1 + iva1
    total2 = subtotal2 - descuento2 + iva2

    total_compra = calcular_total_productos(total1, total2)

    return (
        subtotal1, descuento1, iva1, total1,
        subtotal2, descuento2, iva2, total2, total_compra
    )


def mostrar_factura(
    nombre,
    nombre1, precio1, cantidad1, porcentaje1, impuesto1,
    total1, subtotal1, descuento1, iva1,
    nombre2, precio2, cantidad2, porcentaje2, impuesto2,
    total2, subtotal2, descuento2, iva2,
    total_compra
):
    print("\n========== FACTURA ==========")
    print("Cliente:", nombre)

    print("\nPRODUCTO 1:", nombre1)
    print(f"Precio unitario: C$ {precio1:.2f}")
    print("Cantidad:", cantidad1)
    print(f"Subtotal: C$ {subtotal1:.2f}")
    print(f"Descuento ({porcentaje1}%): C$ {descuento1:.2f}")
    print(f"IVA ({impuesto1}%): C$ {iva1:.2f}")
    print(f"Total: C$ {total1:.2f}")

    print("\nPRODUCTO 2:", nombre2)
    print(f"Precio unitario: C$ {precio2:.2f}")
    print("Cantidad:", cantidad2)
    print(f"Subtotal: C$ {subtotal2:.2f}")
    print(f"Descuento ({porcentaje2}%): C$ {descuento2:.2f}")
    print(f"IVA ({impuesto2}%): C$ {iva2:.2f}")
    print(f"Total: C$ {total2:.2f}")

    print(f"\nTOTAL DE LA COMPRA: C$ {total_compra:.2f}")


def main():
    nombre = leer_cliente()

    print("\n--- DATOS DEL PRODUCTO 1 ---")
    nombre1 = input("Nombre del producto: ")
    precio1 = float(input("Precio unitario C$: "))
    cantidad1 = int(input("Cantidad: "))
    porcentaje1 = float(input("Porcentaje de descuento: "))
    impuesto1 = float(input("Porcentaje de IVA: "))

    print("\n--- DATOS DEL PRODUCTO 2 ---")
    nombre2 = input("Nombre del producto: ")
    precio2 = float(input("Precio unitario C$: "))
    cantidad2 = int(input("Cantidad: "))
    porcentaje2 = float(input("Porcentaje de descuento: "))
    impuesto2 = float(input("Porcentaje de IVA: "))

    (
        subtotal1, descuento1, iva1, total1,
        subtotal2, descuento2, iva2, total2, total_compra
    ) = calcular_total(
        precio1, cantidad1, porcentaje1, impuesto1,
        precio2, cantidad2, porcentaje2, impuesto2
    )

    mostrar_factura(
        nombre,
        nombre1, precio1, cantidad1, porcentaje1, impuesto1,
        total1, subtotal1, descuento1, iva1,
        nombre2, precio2, cantidad2, porcentaje2, impuesto2,
        total2, subtotal2, descuento2, iva2,
        total_compra
    )


main()