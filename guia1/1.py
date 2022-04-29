def ej1():
    print("ej1")
    listaGene = [1,7,3,9,2,5,8,4,6]
    try:
        holder = int(input("numero a buscar: "))
        
        return f"tu numero esta en el index: {listaGene.index(holder) + 1}"
        
    except:
        return "not found"

print(ej1())