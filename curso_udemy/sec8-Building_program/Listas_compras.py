
print("Bienvenido a tu creador de listas de compras inteligente")
print()
print("1. Crear lista de compras")
print("2. Salir")
opcion = int(input("Digite una opción: "))

if opcion == 1:
    productos = {}
    while True:
        producto = input("Producto: ")
        cantidad = int(input("Cantidad: "))
        if cantidad <= 0:
            print("La cantidad no puede ser menor o igual a 0")
            continue
        productos[producto] = cantidad  # Guardar antes de preguntar si sigue

        print("1. Salir")
        print("2. Continuar")
        continuar = int(input("¿Desea continuar?: "))
        if continuar == 1:
            print(f"\nLista final de compras: {productos}")
            break
elif opcion == 2:
    print("Gracias por visitarnos, vuelva pronto.")
else:
    print("Opción no válida. Intente nuevamente.")


