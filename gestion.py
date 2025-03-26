
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
