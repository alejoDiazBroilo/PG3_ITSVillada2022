archivo = open("./guia3/trabajo5.txt", "w")
def ej1():
    myBool = True
    while myBool:
        try:
            dato1 = str(input("_dame dato str para que no tire error: "))
            dato2 = input("_dame dato int para que tire error: ")
            archivo.write(dato1)
            archivo.write(" / mensaje guardad\n")
            archivo.write(dato2)
            archivo.write(" / mensaje guardad\n")

            if(int(input("_desea continuar? Any Key = si / 1 = no: " )) == 1):
                myBool = False
            else:
                myBool = True
        except ValueError as datoQueNoEsNumero:
            print("*dato ingresado no valido" + str(datoQueNoEsNumero))
        except TypeError as datoQueNoEsNumero:
            print("*TEOOOOOOOOOOOOOOOOOOOOOOOOOOOOO no se pueden poner ints en un txt")
        
ej1()
archivo.close()