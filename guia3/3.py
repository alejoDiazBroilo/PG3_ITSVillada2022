def ej1():
    meses: tuple = ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")
    myBool = True 
    while myBool:
        try:
            dato1 = int(input("que numero desea acceder "))
            print("*mes = " , meses[int(dato1)])
            if(int(input("_desea continuar? Any Key = si / 1 = no: " )) == 1):
                myBool = False
            else:
                myBool = True
        except ValueError:
            print("*dato ingresado no valido")
        except IndexError:
            print("*indice fuera de rango")
        except BaseException:
            print("*error desconocido")
        
ej1()