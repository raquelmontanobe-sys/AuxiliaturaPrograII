import math
from abc import ABC, abstractmethod
class Figura(ABC):
    def __init__(self, color: str):
        self._color = color
    @abstractmethod
    def _obtenerArea(self) -> float:
        pass
    @property
    def color(self) -> str:
        return self._color
class Cuadrado(Figura):
    def __init__(self, color: str, lado: int):
        super().__init__(color)
        self.__lado = lado
    def _obtenerArea(self) -> float:
        return self.__lado ** 2
class Triangulo(Figura):
    def __init__(self, color: str, lado1: int, lado2: int, lado3: int):
        super().__init__(color)
        self.__lado1 = lado1
        self.__lado2 = lado2
        self.__lado3 = lado3
    def _obtenerArea(self) -> float:
        s = (self.__lado1 + self.__lado2 + self.__lado3) / 2
        area = math.sqrt(s * (s - self.__lado1) * (s - self.__lado2) * (s - self.__lado3))
        return area
class Redondo(Figura):
    def __init__(self, color: str, radio: int):
        super().__init__(color)
        self.__radio = radio
    def _obtenerArea(self) -> float:
        return math.pi * (self.__radio ** 2)
cuadrado1 = Cuadrado("Rojo", 4)
cuadrado2 = Cuadrado("Azul", 5)
triangulo1 = Triangulo("Verde", 3, 4, 5)
triangulo2 = Triangulo("Amarillo", 6, 8, 10)
redondo1 = Redondo("Negro", 3)
redondo2 = Redondo("Blanco", 7)
print(f"Cuadrado 1 ({cuadrado1.color}): Área = {cuadrado1._obtenerArea()}")
print(f"Cuadrado 2 ({cuadrado2.color}): Área = {cuadrado2._obtenerArea()}")
print(f"Triángulo 1 ({triangulo1.color}): Área = {triangulo1._obtenerArea()}")
print(f"Triángulo 2 ({triangulo2.color}): Área = {triangulo2._obtenerArea()}")
print(f"Redondo 1 ({redondo1.color}): Área = {redondo1._obtenerArea():.2f}")
print(f"Redondo 2 ({redondo2.color}): Área = {redondo2._obtenerArea():.2f}\n")
cuadrado_evaluado = cuadrado2
triangulo_evaluado = triangulo1
if cuadrado_evaluado._obtenerArea() > triangulo_evaluado._obtenerArea():
    print(f"La figura con mayor área es de color: {cuadrado_evaluado.color}")
elif triangulo_evaluado._obtenerArea() > cuadrado_evaluado._obtenerArea():
    print(f"La figura con mayor área es de color: {triangulo_evaluado.color}")
else:
    print("Ambas figuras tienen la misma área exacta.")