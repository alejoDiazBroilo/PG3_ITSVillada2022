class Persona:
    def __init__(self, name: str, age: int):
        self.nombre = name
        self.age = age

    def changeAge(self, newAge: int):
        self.age = newAge

    def changeName(self, newName: str):
        self.nombre = newName

    def Name(self) -> str:
        return str(self.nombre)

    def Age(self) -> int:
        return int(self.age)

class Empleado(Persona):
    def __init__(self, name: str, age: int, salario: int):
        super().__init__(name, age)
        self.salario = salario

    def changeSalary(self, newSalario: int):
        self.salario = newSalario

    def Salary(self) -> int:
        return int(self.salario)

emp1 = Empleado("Juan", 30, 1000)



        

