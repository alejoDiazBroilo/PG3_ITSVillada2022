def ej1():
    myBool = True
    while myBool:
        try:
            dato1 = int(input("_dame dato 1: "))
            dato2 = int(input("_dame dato 2: "))

            print("*suma = " , dato1 + dato2)

            if(int(input("_desea continuar? Any Key = si / 1 = no: " )) == 1):
                myBool = False
            else:
                myBool = True
        except ValueError as datoQueNoEsNumero:
            print("*dato ingresado no valido" + str(datoQueNoEsNumero))
        except BaseException as datoQueNoEsNumero:
            print("*error desconocido" + str(datoQueNoEsNumero))
        
ej1()