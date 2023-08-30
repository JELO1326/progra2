class Libro:
    def __init__(self, id_libro, titulo, autor):
        self.id_libro = id_libro
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

class Usuario:
    def __init__(self, id_usuario, nombre):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.libros_prestados = []
        self.historial_prestamos = []

class Prestamo:
    def __init__(self, libro, fecha_prestamo, fecha_devolucion=None):
        self.libro = libro
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion

class Catalogo:
    def __init__(self):
        self.libros = []
        self.usuarios = []
        self.prestamos = []


    def agregar_libro(self, id_libro, titulo, autor):
        libro = Libro(id_libro, titulo, autor)
        self.libros.append(libro)

    def eliminar_libro(self, id_libro):
        libro = self.obtener_libro_por_id(id_libro)
        if libro:
            self.libros.remove(libro)

    def registrar_usuario(self, id_usuario, nombre):
        usuario = Usuario(id_usuario, nombre)
        self.usuarios.append(usuario)

    def prestar_libro(self, id_usuario, id_libro, fecha_prestamo):
        usuario = self.obtener_usuario_por_id(id_usuario)
        libro = self.obtener_libro_por_id(id_libro)

        if usuario and libro and libro.disponible:
            libro.disponible = False
            prestamo = Prestamo(libro, fecha_prestamo)
            usuario.libros_prestados.append(prestamo)
            self.prestamos.append(prestamo)
            usuario.historial_prestamos.append(prestamo)

    def devolver_libro(self, id_usuario, id_libro, fecha_devolucion):
        usuario = self.obtener_usuario_por_id(id_usuario)
        libro = self.obtener_libro_por_id(id_libro)

        if usuario and libro:
            for prestamo in usuario.libros_prestados:
                if prestamo.libro == libro:
                    libro.disponible = True
                    prestamo.fecha_devolucion = fecha_devolucion
                    usuario.libros_prestados.remove(prestamo)
                    break

    def consultar_libros_disponibles(self):
        return [libro for libro in self.libros if libro.disponible]

    def ver_historial_prestamos(self):
        print("Historial de préstamos:")
        for usuario in self.usuarios:
            for prestamo in usuario.historial_prestamos:
                libro_titulo = prestamo.libro.titulo
                usuario_nombre = usuario.nombre
                fecha_prestamo = prestamo.fecha_prestamo
                fecha_devolucion = prestamo.fecha_devolucion or 'Pendiente'
                print(f"Libro: {libro_titulo}, Usuario: {usuario_nombre}, Fecha de préstamo: {fecha_prestamo}, Fecha de devolución: {fecha_devolucion}")

    def obtener_nombre_usuario_por_libro(self, libro):
        for usuario in self.usuarios:
            for prestamo in usuario.libros_prestados:
                if prestamo.libro == libro:
                    return usuario.nombre
        return "Desconocido"

    def obtener_usuario_por_id(self, id_usuario):
        for usuario in self.usuarios:
            if usuario.id_usuario == id_usuario:
                return usuario
        print("Usuario no encontrado.")
        return None

    def obtener_libro_por_id(self, id_libro):
        for libro in self.libros:
            if libro.id_libro == id_libro:
                return libro
        print("Libro no encontrado.")
        return None


catalogo_biblioteca = Catalogo()


catalogo_biblioteca.agregar_libro(1, "Cien años de soledad", "Gabriel García Márquez")
catalogo_biblioteca.agregar_libro(2, "1984", "George Orwell")
catalogo_biblioteca.agregar_libro(3, "El Señor de los Anillos", "J.R.R. Tolkien")
catalogo_biblioteca.agregar_libro(4, "Harry Potter y la piedra filosofal", "J.K. Rowling")

def mostrar_menu():
    print("===== Menú de Biblioteca =====")
    print("1. Agregar libro")
    print("2. Eliminar libro")
    print("3. Registrar usuario")
    print("4. Prestar libro")
    print("5. Devolver libro")
    print("6. Consultar libros disponibles")
    print("7. Ver historial de préstamos")
    print("8. Salir")
    print("=============================")

while True:
    mostrar_menu()
    opcion = input("Ingrese la opcion que desee realizar: ")

    if opcion == "1":
        id_libro = int(input("Ingrese el ID del libro: "))
        titulo = input("Ingrese el título del libro: ")
        autor = input("Ingrese el autor del libro: ")
        catalogo_biblioteca.agregar_libro(id_libro, titulo, autor)

    elif opcion == "2":
        id_libro = int(input("Ingrese el ID del libro a eliminar: "))
        catalogo_biblioteca.eliminar_libro(id_libro)

    elif opcion == "3":
        id_usuario = int(input("Ingrese el ID del usuario: "))
        nombre = input("Ingrese el nombre del usuario: ")
        catalogo_biblioteca.registrar_usuario(id_usuario, nombre)

    elif opcion == "4":
        id_usuario = int(input("Ingrese el ID del usuario: "))
        id_libro = int(input("Ingrese el ID del libro a prestar: "))
        fecha_prestamo = input("Ingrese la fecha de préstamo: ")
        catalogo_biblioteca.prestar_libro(id_usuario, id_libro, fecha_prestamo)

    elif opcion == "5":
        id_usuario = int(input("Ingrese el ID del usuario: "))
        id_libro = int(input("Ingrese el ID del libro a devolver: "))
        fecha_devolucion = input("Ingrese la fecha de devolución: ")
        catalogo_biblioteca.devolver_libro(id_usuario, id_libro, fecha_devolucion)

    elif opcion == "6":
        libros_disponibles = catalogo_biblioteca.consultar_libros_disponibles()
        print("Libros disponibles:")
        for libro in libros_disponibles:
            print(f"ID: {libro.id_libro}, Título: {libro.titulo}, Autor: {libro.autor}")

    elif opcion == "7":
        catalogo_biblioteca.ver_historial_prestamos()

    elif opcion == "8":
        print("¡Hasta luego!")
        break

    else:
        print("Opción inválida. Por favor, elija una opción válida.")