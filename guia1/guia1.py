from pickle import TRUE
from unittest import case
holder = 0
holder2 = 0

def ej1():
    print("ej1")
    listaGene = [1,7,3,9]
    try:
        holder = int(input("numero a buscar: "))
        
        return f"tu numero esta en el index: {listaGene.index(holder) + 1}"
        
    except:
        return "not found"
def ej2():
    try:
        holder = int(input("año: "))

        if holder % 100 != 0 and (holder % 400 == 0 or holder % 4 == 0):
            return holder , " si es."
        else:
            return holder , " no es."
        
    except:
        return "dame un año valido."
def ej3():
    try:
        holder2 = input("type: ")
        holder = int(input("column: "))
        for i in range(int(input("row: "))):
            return str(holder2[0]) * holder
    except:
        return "ERROR.."


def ej4(arr):
    try:
        print(arr)
        for i in range(len(arr) - 1):
            for j in range(0, len(arr) -i-1):
                if arr[j] > arr[j + 1] :
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr
    except:
        return "ERROR.."


def ej5():
    holder2 = 1
    try:
        holder = str(input("palabra: "))
        for i in range(round(len(holder) / 2)): 
            if holder[i] == holder[len(holder) - 1 - i]:
                pass
            else:
                holder2 = 0
                print(holder, " no es palindromo")
                return(False)
        if holder2 == 1:
            print(holder, " es palindromo")
            return(True)
    except:
        return "ERROR.."

def ej6():
    
    try:
        holder2 = 0
        holder = str(input("palabra: "))
        for i in holder:
            if i.lower() in "aeiouàèìòù":
                holder2 += 1
        return "vocales = " , holder2
    except:
        return "ERROR.."
        

def ej7():
    holder = str(input("numero: "))
    for i in range(holder):
        if not(holder[i] == holder[i] + 1 or holder[i] == holder[i] - 1):
            return "no es step"
    return "es step"
    try:
        print("")
    except:
        return "ERROR.."

#ej4([3,2,6,4,6])
print(ej7())