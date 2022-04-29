def ej3():
    try:
        holder2 = input("type: ")
        holder = int(input("column: "))
        for i in range(int(input("row: "))):
            print(str(holder2[0]) * holder)

        return "DONE.."
    except:
        return "ERROR.."

print(ej3())