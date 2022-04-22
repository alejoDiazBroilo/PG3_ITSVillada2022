from operator import truediv
from pty import slave_open
import re


class Triangulo:
    def __init__(self, lado1: int, lado2: int, lado3: int):
        self.Lado1 = lado1
        self.Lado2 = lado2
        self.Lado3 = lado3
        
    def imprimir(self) -> str:
        return "lado 1 = " + str(self.Lado1) + " lado 2 = " + str(self.Lado2) + " lado 3 = " + str(self.Lado3)
    
    def isEquilatero(self) -> bool:
        if self.Lado1 == self.Lado2 and self.Lado3 == self.Lado2:
            return True
        else:
            return False 

    def ladoGrande(self) -> str:
        if self.Lado1 > self.Lado2 and self.Lado1 > self.Lado3:
            return "mas grande = lado 1"
        elif self.Lado2 > self.Lado1 and self.Lado2 > self.Lado3:
            return "mas grande = lado 2"
        elif self.Lado3 > self.Lado1 and self.Lado3 > self.Lado2:
            return "mas grande = lado 3"

thisTriangulo = Triangulo(input("lado 1: "), input("lado 2: "), input("lado 3: "))

print(thisTriangulo.imprimir())
print(str(thisTriangulo.isEquilatero()))
print(str(thisTriangulo.ladoGrande()))



