class Persona:
    def __init__(self, name: str):
        self.nombre = name
        
    def Name(self) -> str:
        return str(self.nombre)

P1 = Persona(str(input("Which name shall i receive... father: ")))

print(f"my child, as god as my witness, you shall be refered as: {P1.Name()}. Now go, go and feel the world...")