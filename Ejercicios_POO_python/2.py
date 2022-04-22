class Alumno:
    def __init__(self, name: str):
        self.nombre = name
        self.nota = 11
        
    def Name(self) -> str:
        return str(self.nombre)

    def Grade(self, nota_actual: int):
        if int(nota_actual) < 10 and int(nota_actual) >= 0:
            self.nota = nota_actual
            print("The grade has been assigned")

        else:   
            print("nota no valida, no se asignara ningun valor")    

    def TestGrade(self)  -> str:
        if int(self.nota) > 10:
            return "you haven`t assigned a grade yet"

        if int(self.nota) >= 5:
            return "Good job " + self.nombre  + "."
        else:
            return f"{self.nombre}, your performance has been deplorable and un worthy of your capabilities. you are a disgrace and you shall be terminated from the phase of this world"

P1 = Alumno(str(input("Which name shall i receive... father: ")))
print("the name that YOU, my father gave me is: " + P1.Name())
P1.Grade(input("nota trabajo: "))
print(P1.TestGrade())