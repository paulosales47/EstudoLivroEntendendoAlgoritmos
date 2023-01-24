def quicksort(array):
    if(len(array) < 2):
        return array
    
    pivo = array[0]
    print(array)
    menores = [i for i in array[1: ] if i <= pivo] 
    maiores = [i for i in array[1: ] if i > pivo]

    return quicksort(menores) + [pivo] + quicksort(maiores)

def quicksortPivoCentral(array):
    if(len(array) < 2):
        return array
    
    pivo = array[len(array)//2]
    print(array)
    menores = [i for i in array[:] if i < pivo] 
    maiores = [i for i in array[:] if i > pivo]

    return quicksortPivoCentral(menores) + [pivo] + quicksortPivoCentral(maiores)


# minha_lista = [12, 35, 0, 7, 4, 45, 69, 23, 78, 1, 2, 3, 4, 79, 0, 69, 25, 87, 3, 1, -785]
# print(quicksort(minha_lista))

minha_lista = list(range(0, 9))

print(quicksort(minha_lista))
print('--------------------------------------')
print(quicksortPivoCentral(minha_lista))

#print([i for i in list(range(0, 101)) if i%2 == 0])

