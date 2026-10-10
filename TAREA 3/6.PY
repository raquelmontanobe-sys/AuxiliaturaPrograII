import copy
class Animal:
    def __init__(self, edad: int, peso: float, especie: str):
        self._edad = edad
        self._peso = peso
        self._especie = especie
    def respirar(self) -> str:
        return f"{self._especie} toma oxígeno del entorno."
    def mover(self) -> str:
        return f"{self._especie} se desplaza por su hábitat."
    def mostrar_datos(self):
        print(f"Especie: {self._especie}, Edad: {self._edad} años, Peso: {self._peso} kg")
class Terrestre(Animal):
    def __init__(self, edad: int, peso: float, especie: str, nro_patas: int, tipo_terreno: str):
        super().__init__(edad, peso, especie)
        self.__nro_patas = nro_patas
        self.__tipo_terreno = tipo_terreno
    def caminar(self):
        return f"{self._especie} está caminando sobre {self.__nro_patas} patas."
    def excavar(self):
        return f"{self._especie} está excavando en terreno {self.__tipo_terreno}."
    def respirar(self) -> str:
        base = super().respirar()
        return f"{base} Específicamente, inhala aire hacia sus pulmones."
    def mover(self) -> str:
        return f"{self._especie} se mueve caminando o corriendo sobre la tierra."
class Acuatico(Animal):
    def __init__(self, edad: int, peso: float, especie: str, tipo_agua: str, profundidad_max: float):
        super().__init__(edad, peso, especie)
        self.__tipo_agua = tipo_agua
        self.__profundidad_max = profundidad_max
    def nadar_profundo(self):
        return f"{self._especie} bucea hasta {self.__profundidad_max} metros."
    def camuflarse(self):
        return f"{self._especie} se camufla en aguas {self.__tipo_agua}."
    def respirar(self) -> str:
        base = super().respirar()
        return f"{base} Específicamente, filtra el oxígeno disuelto en el agua a través de sus branquias."
    def mover(self) -> str:
        return f"{self._especie} se mueve nadando usando sus aletas."
class Aereo(Animal):
    def __init__(self, edad: int, peso: float, especie: str, envergadura: float, plumaje: str):
        super().__init__(edad, peso, especie)
        self.__envergadura = envergadura
        self.__plumaje = plumaje
    def planear(self):
        return f"{self._especie} planea usando su envergadura de {self.__envergadura}m."
    def acicalar(self):
        return f"{self._especie} está limpiando su plumaje color {self.__plumaje}."
    def respirar(self) -> str:
        base = super().respirar()
        return f"{base} Específicamente, utiliza sacos aéreos para maximizar la absorción durante el vuelo."
    def mover(self) -> str:
        return f"{self._especie} se mueve volando por los cielos."
leon = Terrestre(5, 190.5, "León", 4, "Sabana")
tiburon = Acuatico(8, 900.0, "Tiburón Blanco", "Salada", 1200)
aguila = Aereo(3, 6.5, "Águila Real", 2.3, "Café dorado")
for animal in [leon, tiburon, aguila]:
    animal.mostrar_datos()
    print("- Respiración:", animal.respirar())
    print("- Movimiento:", animal.mover())
    print()