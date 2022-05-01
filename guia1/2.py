def ej2():
    try:
        holder = int(input("año: "))

        if holder % 100 != 0 and (holder % 400 == 0 or holder % 4 == 0):
            return f"{holder}  si es."
        else:
            return f"{holder}  no es."
        
    except:
        return "dame un año valido."

print(ej2())