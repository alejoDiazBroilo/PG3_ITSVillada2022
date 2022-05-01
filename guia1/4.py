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

print(ej4([3,2,6,4,6]))
