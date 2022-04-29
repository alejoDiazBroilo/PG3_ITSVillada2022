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

