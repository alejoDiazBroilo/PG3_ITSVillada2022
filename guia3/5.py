from copyreg import add_extension


archivo = open("./guia3/trabajo5.txt", "w")
def ej1():
    myBool = True
    while myBool:
        try:
            dato1 = str(input("_dame dato str para que no tire error: "))
            dato2 = int(input("_dame dato int para que tire error: "))

            archivo.write(dato1)
            archivo.write(" / mensaje guardado\n")

            archivo.write(dato2)
            archivo.write(" / mensaje guardado\n")
        except ValueError:
            print("*se ingreso un str en dato2 que es un int: ")
        except TypeError:
            print("*TEOOOOOOOOOOOOOOOOOOOOOOOOOOOOO no se pueden poner ints en un txt")
            print(f"*igual el mensaje: {dato1}, se guardo en el txt")
            archivo.close()
        
ej1()
archivo.close()