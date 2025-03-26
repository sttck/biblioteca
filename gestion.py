
class Biblioteca:
    def _init_(self):
        self.rentas = []
        self.libros_prestados = []

    def agregar_renta(self):
        usuario = input("Nombre del usuario: ")
        libro = input("Nombre del libro: ")
        
        # Bloquear préstamo si el libro ya está prestado
        if libro in self.libros_prestados:
            print(f"El libro '{libro}' ya está prestado. No se puede realizar el préstamo.")
            return

        dia_pedido = int(input("Día del pedido: "))
        mes_pedido = int(input("Mes del pedido: "))
        dia_entrega = int(input("Día de entrega: "))
        mes_entrega = int(input("Mes de entrega: "))
        costo = float(input("Costo del préstamo: "))
        
        renta = {
            "usuario": usuario,
            "libro": libro,
            "dia_pedido": dia_pedido,
            "mes_pedido": mes_pedido,
            "dia_entrega": dia_entrega,
            "mes_entrega": mes_entrega,
            "costo": costo
        }
        self.rentas.append(renta)
        self.libros_prestados.append(libro)
        print(f"Renta agregada: {renta}")
        
    def mostrar_rentas(self):
        if not self.rentas:
            print("No hay rentas registradas.")
        else:
            for i, renta in enumerate(self.rentas, 1):
                print(f"\nRenta {i}:")
                print(f"  Usuario: {renta['usuario']}")
                print(f"  Libro: {renta['libro']}")
                print(f"  Fecha del pedido: {renta['dia_pedido']}/{renta['mes_pedido']}")
                print(f"  Fecha de entrega: {renta['dia_entrega']}/{renta['mes_entrega']}")
                print(f"  Costo: ${renta['costo']:.2f}")

    def eliminar_renta(self):
        libro = input("Ingrese el nombre del libro a eliminar: ")
        for renta in self.rentas:
            if renta["libro"] == libro:
                self.rentas.remove(renta)
                self.libros_prestados.remove(libro)
                print(f"La renta del libro '{libro}' ha sido eliminada.")
                return
        print(f"No se encontró ninguna renta del libro '{libro}'.")

    def editar_renta(self):
        libro = input("Ingrese el nombre del libro a editar: ")
        for renta in self.rentas:
            if renta["libro"] == libro:
                print("Ingrese los nuevos datos:")
                renta["usuario"] = input("Nuevo nombre del usuario: ")
                renta["dia_pedido"] = int(input("Nuevo día del pedido: "))
                renta["mes_pedido"] = int(input("Nuevo mes del pedido: "))
                renta["dia_entrega"] = int(input("Nuevo día de entrega: "))
                renta["mes_entrega"] = int(input("Nuevo mes de entrega: "))
                renta["costo"] = float(input("Nuevo costo del préstamo: "))
                print(f"Renta actualizada: {renta}")
                return
        print(f"No se encontró ninguna renta del libro '{libro}'.")

biblioteca = Biblioteca()
## menú para la biblioteca, paara utilizar todo lo de antes
while True:
    print("\n--- Menú ---")
    print("1. Agregar renta")
    print("2. Mostrar rentas")
    print("3. Eliminar renta")
    print("4. Editar renta")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        biblioteca.agregar_renta()
    elif opcion == "2":
        biblioteca.mostrar_rentas()
    elif opcion == "3":
        biblioteca.eliminar_renta()
    elif opcion == "4":
        biblioteca.editar_renta()
    elif opcion == "5":
        print("¡Adiós!")
        break
    else:
        print("Opción no válida. Intente de nuevo.")