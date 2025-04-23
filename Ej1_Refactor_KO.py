# Sistema de venta de billetes de avión

class Vuelo:
    def __init__(self, numero_vuelo, origen, destino, fecha, salida, llegada, precio):
        self.numero_vuelo = numero_vuelo
        self.origen = origen
        self.destino = destino
        self.fecha = fecha
        self.salida = salida
        self.llegada = llegada
        self.precio = precio

class Pasajero:
    def __init__(self, nombre, apellido, edad, telefono, correo):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.telefono = telefono
        self.correo = correo

class Informacion:
    def __init__(self, vuelo, pasajero, asientos):
        self.vuelo = vuelo
        self.pasajero = pasajero
        self.asientos = asientos

def mostrar_vuelos_disponibles(vuelos):
    print("Vuelos disponibles:")
    for vuelo in vuelos:
        print(f"Número de vuelo: {vuelo.numero_vuelo}, Origen: {vuelo.origen}, Destino: {vuelo.destino}, Fecha: {vuelo.fecha}, Hora de salida: {vuelo.salida}, Hora de llegada: {vuelo.llegada}, Precio: {vuelo.precio}")

def reservar_vuelo(lista, numero, pasajero, cantidad):
    
    for vuelo in lista:
        if vuelo.numero == numero:
            if cantidad <= 0:
                print("La cantidad de asientos debe ser mayor que cero.")
                return
            elif cantidad > 10:
                print("Lo sentimos, no se pueden reservar más de 10 asientos por reserva.")
                return
            elif cantidad > 0 and cantidad <= 10:
                reserva = Informacion(vuelo, pasajero, cantidad)
                print(f"¡Reserva exitosa para el vuelo {vuelo.numero_vuelo}!")
                print(f"Nombre del pasajero: {pasajero.nombre} {pasajero.apellido}, Asientos reservados: {cantidad}")
                return
    print("No se encontró ningún vuelo con el número especificado.")

def capturar_datos_pasajero():
            nombre = input("Ingrese su nombre: ")
            apellido = input("Ingrese su apellido: ")
            edad = int(input("Ingrese su edad: "))
            telefono = input("Ingrese su número de teléfono: ")
            correo = input("Ingrese su correo electrónico: ")
            return Pasajero(nombre, apellido, edad, telefono, correo)

def capturar_datos_reserva():
    numero_vuelo = input("Ingrese el número de vuelo que desea reservar: ")
    try:
        cantidad = int(input("Ingrese la cantidad de asientos que desea reservar (máximo 10): "))
    except ValueError:
        print("Debe ingresar un número válido de asientos.")
        return None, None
    return numero_vuelo, cantidad



def main():
    vuelos = [
        Vuelo("AA123", "Nueva York", "Los Angeles", "2024-05-15", "08:00", "11:00", 250.00),
        Vuelo("AA456", "Los Angeles", "Chicago", "2024-05-20", "10:00", "13:00", 200.00),
        Vuelo("AA789", "Chicago", "Miami", "2024-05-25", "12:00", "15:00", 300.00)
    ]

    print("Bienvenido al sistema de venta de billetes de avión.")
    opcion = input("Seleccione una opción:\n1. Ver vuelos disponibles\n2. Reservar vuelo\nIngrese su opción: ")

    if opcion == '1':
        mostrar_vuelos_disponibles(vuelos)
    elif opcion == '2':
        pasajero = capturar_datos_pasajero()

        numero, cantidad = capturar_datos_reserva()
        if numero is None or cantidad is None:
            return

    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()
