class Computadora:
    def __init__(self, marca, procesador, ram, almacenamiento):
        self.marca=marca
        self.procesador=procesador
        self.ram=ram
        self.almacenamiento=almacenamiento
    def compararRAM(self, x):
        if self.ram==x:
            print("La RAM es igual a", x, "GB")
        else:
            print("La RAM no es igual a", x, "GB")
    def mostrarDatos(self):
        print("Marca:", self.marca)
        print("Procesador:", self.procesador)
        print("RAM:", self.ram, "GB")
        print("Almacenamiento:", self.almacenamiento, "GB")
computadora1=Computadora("HP", "Intel i5", 8, 500)
computadora2=Computadora(
    marca="Lenovo",
    procesador="Ryzen 5",
    ram=16,
    almacenamiento=1000
)
computadora1.compararRAM(8)
computadora2.compararRAM(8)
if computadora1.almacenamiento > computadora2.almacenamiento:
    computadora1.mostrarDatos()
else:
    computadora2.mostrarDatos()