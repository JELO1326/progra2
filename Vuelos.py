class Avion:
    def __init__(self, modelo, num_asientos):
        self.modelo = modelo
        self.num_asientos = num_asientos

class Vuelo:
    def __init__(self, num_vuelo, origen, destino, fecha_hora, avion):
        self.num_vuelo = num_vuelo
        self.origen = origen
        self.destino = destino
        self.fecha_hora = fecha_hora
        self.avion = avion
        self.reservaciones = []

class Pasajero:
    def __init__(self, nombre, num_pasaporte):
        self.nombre = nombre
        self.num_pasaporte = num_pasaporte
        self.reservaciones = []

class Reservacion:
    def __init__(self, num_reservacion, pasajero, vuelo):
        self.num_reservacion = num_reservacion
        self.pasajero = pasajero
        self.vuelo = vuelo
        self.estado = "reservado"

class SistemaReservaciones:
    def __init__(self):
        self.vuelos_disponibles = []
        self.reservaciones = []
        self.pasajeros = []


    def crear_vuelo(self, num_vuelo, origen, destino, fecha_hora, avion):
        vuelo = Vuelo(num_vuelo, origen, destino, fecha_hora, avion)
        self.vuelos_disponibles.append(vuelo)

    def mostrar_vuelos_disponibles(self):
        print("Vuelos disponibles:")
        for vuelo in self.vuelos_disponibles:
            print(f"Vuelo {vuelo.num_vuelo} - {vuelo.origen} a {vuelo.destino} - {vuelo.fecha_hora}")

    def reservar_vuelo(self, pasajero, vuelo):
        if vuelo.avion.num_asientos > len(vuelo.reservaciones):
            if vuelo not in pasajero.reservaciones:
                for reservacion in self.reservaciones:
                    if reservacion.pasajero.num_pasaporte == pasajero.num_pasaporte:
                        print("El pasaporte ya está en uso en una reserva.")
                        return
                
                reservacion = Reservacion(len(self.reservaciones) + 1, pasajero, vuelo)
                vuelo.reservaciones.append(reservacion)
                pasajero.reservaciones.append(reservacion)
                self.reservaciones.append(reservacion)
                print("Reservación exitosa.")
            else:
                print("Ya tienes una reserva en este vuelo.")
        else:
            print("Lo sentimos, no hay asientos disponibles en este vuelo.")

    def cancelar_reservacion(self, pasajero, num_reservacion):
        for reservacion in pasajero.reservaciones:
            if reservacion.num_reservacion == num_reservacion and reservacion.estado == "reservado":
                reservacion.estado = "cancelado"
                print("Reservación cancelada.")
                pasajero.reservaciones.remove(reservacion)
                vuelo = reservacion.vuelo
                vuelo.reservaciones.remove(reservacion)
                return
        print("No se encontró una reservación válida para cancelar.")

    def mostrar_reservaciones_pasajero(self, pasajero):
        print(f"Reservaciones de {pasajero.nombre}:")
        for reservacion in pasajero.reservaciones:
            print(f"Vuelo {reservacion.vuelo.num_vuelo} - Estado: {reservacion.estado}")

    def mostrar_pasajeros_vuelo(self, vuelo):
        print(f"Pasajeros en el vuelo {vuelo.num_vuelo}:")
        for reservacion in vuelo.reservaciones:
            print(reservacion.pasajero.nombre)


sistema = SistemaReservaciones()


avion1 = Avion("Boeing 737", 150)
avion2 = Avion("Airbus A320", 180)
avion3 = Avion("Boeing 777", 301)
avion4 = Avion("Airbus A340", 600)

sistema.crear_vuelo("RR132", "Chile", "Japon", "2023-09-01 10:00", avion1)
sistema.crear_vuelo("BB456", "Temuco", "Iquique", "2023-09-02 12:00", avion2)
sistema.crear_vuelo("KL500","Chile", "Andorra", "2023-10-12 13:00", avion3)
sistema.crear_vuelo("CC002", "Chile", "Paris", "2023-12-12 18:00", avion4)


num_pasajeros = int(input("Ingresa el número de pasajeros: "))
for _ in range(num_pasajeros):
    nombre = input("Ingresa el nombre del pasajero: ")
    num_pasaporte = input("Ingresa el número de pasaporte del pasajero: ")
    pasajero = Pasajero(nombre, num_pasaporte)
    sistema.pasajeros.append(pasajero)

def mostrar_menu():
    print("===== Bienvenido/a al Sistema de Reservaciones =====")
    print("1. Consultar vuelos disponibles")
    print("2. Reservar un vuelo")
    print("3. Cancelar un vuelo")
    print("4. Ver tus Reservaciones")
    print("5. Ver pasajeros en un vuelo")
    print("6. Salir")
    print("=============================")

while True:
    mostrar_menu()
    opcion = input("Ingrese el número de la opción que desea realizar: ")
    if opcion == "1":
        sistema.mostrar_vuelos_disponibles()
    elif opcion == "2":
        pasaporte = input("Ingresa tu número de pasaporte: ")
        for pasajero in sistema.pasajeros:
            if pasajero.num_pasaporte == pasaporte: #verificacion para saber si esta en uso o no un pasaporte 
                sistema.mostrar_vuelos_disponibles()
                num_vuelo = input("Ingresa el número de vuelo que deseas reservar: ")
                for vuelo in sistema.vuelos_disponibles:
                    if vuelo.num_vuelo == num_vuelo:
                        sistema.reservar_vuelo(pasajero, vuelo)
                        break
                else:
                    print("Vuelo no encontrado.")
                break
        else:
            print("Pasajero no encontrado.")
    elif opcion == "3":
        pasaporte = input("Ingresa tu número de pasaporte: ")
        for pasajero in sistema.pasajeros:
            if pasajero.num_pasaporte == pasaporte:
                sistema.mostrar_reservaciones_pasajero(pasajero)
                num_reservacion = int(input("Ingresa el número de reservación que deseas cancelar: "))
                sistema.cancelar_reservacion(pasajero, num_reservacion)
                break
        else:
            print("Pasajero no encontrado.")
    elif opcion == "4":
        pasaporte = input("Ingresa tu número de pasaporte: ")
        for pasajero in sistema.pasajeros:
            if pasajero.num_pasaporte == pasaporte:
                sistema.mostrar_reservaciones_pasajero(pasajero)
                break
        else:
            print("Pasajero no encontrado.")
    elif opcion == "5":
        sistema.mostrar_vuelos_disponibles()
        num_vuelo = input("Ingresa el número de vuelo para ver la lista de pasajeros: ")
        for vuelo in sistema.vuelos_disponibles:
            if vuelo.num_vuelo == num_vuelo:
                sistema.mostrar_pasajeros_vuelo(vuelo)
                break
        else:
            print("Vuelo no encontrado.")
    elif opcion == "6":
        print("Gracias por usar el Sistema de Reservaciones. ¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")