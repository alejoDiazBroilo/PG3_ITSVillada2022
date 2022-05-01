def ej7():
    esStep = True
    try:
        holder = str(input("numero: "))
        if len(holder) % 2 != 0:
            return "no es par, no se permite"
        else:
            for i in range(len(holder) - 1):
                print(f"{holder[i]} - {holder[i + 1]} = {abs(int(holder[i]) - int(holder[i + 1]))}")
                if abs(int(holder[i]) - int(holder[i + 1])) == 1:
                    pass
                else:
                    esStep = False
                    break
        return f"es step? RTA: {esStep}"
    except:
        return "ERROR.."

print(ej7())