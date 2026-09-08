class Bus:
    def __init__(self, capacidad):
        self.capacidad=capacidad
        self.pasajeros=0
        self.dinero=0
    def subirPasajeros(self, cantidad):
        if self.pasajeros+cantidad<=self.capacidad:
            self.pasajeros=self.pasajeros+cantidad
            print("Subieron", cantidad)
        else:
            print("Error: no hay suficientes asientos")
    def cobrarPasaje(self):
        dinero=self.pasajeros*1.50
        self.dinero=self.dinero+dinero
        print("Se cobró:", dinero)
    def asientosDisponibles(self):
        disponibles=self.capacidad-self.pasajeros
        print("Asientos disponibles:", disponibles)
bus = Bus(30)
bus.subirPasajeros(10)
bus.cobrarPasaje()
bus.asientosDisponibles()