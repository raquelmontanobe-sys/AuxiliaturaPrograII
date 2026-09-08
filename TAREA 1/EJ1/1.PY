class Auto:
    def __init__(self, marca, modelo, anio, kilometraje, color):
        self.marca=marca
        self.modelo=modelo
        self.anio=anio
        self.kilometraje=kilometraje
        self.color=color
    def mostrarKilometraje(self):
        km=self.kilometraje
        metros=km*1000
        print("Kilometraje:", km, "km =", metros, "metros")
    def cambiarColor(self, nuevoColor):
        self.color=nuevoColor
auto1=Auto("Toyota", "Corolla", 2020, 50000, "Rojo")
auto2=Auto("Nissan", "Versa", 2022, 30000, "Azul")
auto1.cambiarColor("Negro")
auto2.cambiarColor("Blanco")
auto1.mostrarKilometraje()
auto2.mostrarKilometraje()