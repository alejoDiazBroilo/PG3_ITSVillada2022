import mysql.connector
def ej1():
    try:
        mydb = mysql.connector.connect(
            host = str(input("_dame host: / el host de mi pc es: 'localhost': ")),
            user = str(input("_dame user: / el user de mi pc es: 'bdi': ")),
            password = str(input("_dame password: / el password de mi pc es: 'pepe1234': ")),
        )
        print("*conexion exitosa: " + str(mydb))

        mydb.database = str(input("_dame nombre de la base de datos: "))

        mycursor = mydb.cursor()

        mycursor.execute("CREATE TABLE " + str(input('*vamos a usar una libreria generica\n_dame el nombre de la tabla: ')) + " (name VARCHAR(255), address VARCHAR(255))") 
        print("*tabla creada")

        while True:
            if(input("_desea borrar una tabla(NOTA: LAS BORRA ENSERIO, por las dudas aviso)? Any Key = si / 0 = no: ") == "0"):
                print("*fin del programa..")
                break
            else:
                mycursor.execute("DROP TABLE " + str(input('_dame el nombre de la tabla: ')))
                print("*tabla borrada")
        mydb.close()

    except ValueError as datoQueNoEsNumero:
        print("*dato ingresado no valido: " + str(datoQueNoEsNumero))
    
    except mysql.connector.Error as error:
        print("*error al conectar a la base de datos: " + str(error))
            
ej1()

