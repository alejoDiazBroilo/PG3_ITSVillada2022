from unittest import case
holder = 0

def ej1():
    print("ej1")
    listaGene = [1,7,3,9]
    try:
        holder = int(input("numero a buscar: "))
        
        print(f"tu numero esta en el index: {listaGene.index(holder) + 1}")
        
    except:
        print("not found")
def ej2():
    try:
        holder = int(input("año: "))

        if holder % 100 != 0 and (holder % 400 == 0 or holder % 4 == 0):
            print(holder , " si es.")
        else:
            print(holder , "no es.")
        
    except:
        print("dame un año valido.")
def ej3():
    try:
        holder2 = input("type: ")
        holder = int(input("column: "))
        for i in range(int(input("row: "))):
            print(str(holder2[0]) * holder)
    except:
        print("ERROR..")

def ej4(arr):
    try:
        print(arr)
        for i in range(len(arr) - 1):
            for j in range(0, len(arr) -i-1):
                if arr[j] > arr[j + 1] :
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print(arr)
    except:
        print("ERROR..")

def ej5():
        holder = str(input("palabra: "))
        holder2 = len(holder)
        holder2 = holder2 / 2
        for i in round(range(str(holder)) / 2):
            print(holder)
        try:
            print(2)
        except:
            print("ERROR..")

#ej4([3,2,6,4,6])
ej5()
