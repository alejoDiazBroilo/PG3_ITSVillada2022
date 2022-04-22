class Calculadora:
    def __init__(self, numero1: int, numero2: int):
        self.Numero1 = numero1
        self.Numero2 = numero2

        print(self.Suma())
        print(self.Resta())
        print(self.multiplicacion())
        print(self.Division())

        
    def Suma(self) -> int:
        return self.Numero1 + self.Numero2

    def Resta(self) -> int:
        return self.Numero1 - self.Numero2

    def multiplicacion(self):
        return self.Numero1 * self.Numero2

    def Division(self):
        if self.Numero2 != 0:
            return self.Numero1 / self.Numero2
        else:
            return "no se puede dividir entre 0"

cacl = Calculadora(int(input("dame dato 1: ")), int(input("dame dato 2: ")))

        

