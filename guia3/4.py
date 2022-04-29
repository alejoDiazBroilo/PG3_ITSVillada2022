def ej1():
    myBool = True
    while myBool:
        try:
            dato1 = int(input("_dame dato 1: "))
            dato2 = int(input("_dame dato 2: "))

            print("*division = " , dato1 / dato2)

            if(int(input("_desea continuar? Any Key = si / 1 = no: " )) == 1):
                print("*fin del programa..")
                myBool = False
            else:
                print("*continuar")
                myBool = True
        except ValueError as datoQueNoEsNumero:
            print("*dato ingresado no valido: " + str(datoQueNoEsNumero))
        except ZeroDivisionError as datoQueNoEsZero:
            print("*no se puede dividir entre 0: " + str(datoQueNoEsZero))
        except BaseException as datoQueNoEsNumero:
            print("*error desconocido: " + str(datoQueNoEsNumero))
        
ej1()