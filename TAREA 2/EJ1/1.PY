class Auto:
    def __init__(self, marca="Sin marca", color="Sin color", gasolina=0):
        self.marca=marca
        self.color=color
        self.gasolina=gasolina
    def __pos__(self):
        self.gasolina=self.gasolina + 5
        return self
    def __add__(self, color):
        self.color=color
        return self
    def __sub__(self, otro):
        return self.gasolina+otro.gasolina
    def mostrar(self):
        print("Marca:", self.marca)
        print("Color:", self.color)
        print("Gasolina:", self.gasolina, "litros")
auto1=Auto("Toyota", "Rojo", 20)
auto2=Auto()
auto2.marca="Ford"
auto2.color="Azul"
auto2.gasolina=15
print("AUTO 1")
auto1.mostrar()
print("AUTO 2")
auto2.mostrar()
+auto1
print("AUTO 1 CON 5 LITROS MÁS")
auto1.mostrar()
auto1 + "Verde"
print("AUTO 1 CON NUEVO COLOR")
auto1.mostrar()
total = auto1 - auto2
print("TOTAL DE GASOLINA:", total, "litros")

