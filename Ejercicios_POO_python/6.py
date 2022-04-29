class Familia: 
    def __init__(self, hijos, padre: str, madre: str):
        self.padre = padre
        self.madre = madre
        self.hijos = hijos
    def __str__(self):
        return f"Padre: {self.padre} \nMadre: {self.madre} \nHijos: {self.Hijos()}"
    def Hijos(self):
        strToPrint = ""
        for i in self.hijos:
            strToPrint = strToPrint + ", " + i
        return strToPrint
        

flia1 = Familia(["teo", "luciano"], "Luciano grande", "Teo grande")
print(flia1)