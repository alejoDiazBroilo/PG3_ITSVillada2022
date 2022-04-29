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

print(ej5())