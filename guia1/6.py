def ej6():
    try:
        holder2 = 0
        holder = str(input("palabra: "))
        for i in holder:
            if i.lower() in "aeiouàèìòù":
                holder2 += 1
        return f"vocales =  {holder2}"
    except:
        return "ERROR.."

print(ej6())