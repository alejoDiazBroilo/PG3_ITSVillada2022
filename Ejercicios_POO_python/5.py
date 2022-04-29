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

emp1 = Empleado("Teo", 30, 1000)
print(f"el empleado {emp1.Name()}, tiene {emp1.Age()} anios y tiene un salario de {emp1.Salary()}")
emp1.changeSalary(2000)
emp1.changeName("Teo mas viejo")
emp1.changeAge(40)
print(f"el empleado {emp1.Name()}, tiene {emp1.Age()} anios y tiene un salario de {emp1.Salary()}")


emp2 = Empleado(input("Nombre empleado: "), input("Edad del empleado: "), input("Salario del empleado: "))

print(f"el empleado {emp2.Name()}, tiene {emp2.Age()} anios y tiene un salario de {emp2.Salary()}")
emp2.changeName(input("Nombre empleado: "))
emp2.changeAge(input("Edad del empleado: "))
emp2.changeSalary(input("Salario del empleado: "))
print(f"el empleado {emp2.Name()}, tiene {emp2.Age()} anios y tiene un salario de {emp2.Salary()}")




        

