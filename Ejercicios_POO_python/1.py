class Persona:
    def __init__(self, name: str):
        self.nombre = name
        
    def Name(self) -> str:
        return str(self.nombre)

P1 = Persona("Teo")

print("the father shall be called: " + P1.Name())

P1 = Persona(str(input("\nWhich name shall i receive... father: ")))

print(f"_my child, as god as my witness, \n_you shall be refered as: {P1.Name()}. \n_Now go, go and feel the world...")