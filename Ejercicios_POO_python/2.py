class Alumno:
    def __init__(self, name: str):
        self.nombre = name
        self.nota = 11
        
    def Name(self) -> str:
        return str(self.nombre)

    def Grade(self) -> int:
        return self.nota

    def ChangeGrade(self, nota_actual: int):
        if int(nota_actual) < 10 and int(nota_actual) >= 0:
            self.nota = nota_actual
            print("_Nota cambiada a: " + str(self.nota))

        else:   
            print("_Nota no valida, no se asignara ningun valor")    

    def TestGrade(self)  -> str:
        if int(self.nota) > 10:
            return "_You haven`t assigned a grade yet"

        if int(self.nota) >= 5:
            return f"_El alumno {self.Name()} ha aprobado con una nota de {self.nota}"
        else:
            return f"_El alumno {self.Name()} ha desaprobado con una nota de {self.nota}"

P1 = Alumno("Teo")

print(f"*El Alumno se llama: {P1.Name()}")
print("*Al Alumno se le asignara la nota 9")
P1.ChangeGrade(9)
print(f"*El Alumno tiene una nota de: {P1.Grade()}")
print(P1.TestGrade())

print("#" * 10)
P2 = Alumno(str(input("Alumno 2: ")))

print(f"*El Alumno se llama: {P2.Name()}")
P2.ChangeGrade(int(input("*Al Alumno se le asignara la nota: ")))
print(f"*El Alumno tiene una nota de: {P2.Grade()}")
print(P2.TestGrade())