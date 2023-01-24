import time

def fatorial(valor):
    if(valor == 1):
        return 1
    else:
        return valor * fatorial(valor - 1);


def fatorial_tail(valor, total = 1):
    if(valor == 0):
        return total
    else:
        return fatorial_tail(valor - 1, valor * total)

def somarItensArray(array):
    if(len(array) == 0):
        return 0
    
    return array.pop() + somarItensArray(array)

def contarItensArray(array):
    
    if(array == []):
        return -1
    
    array.pop()
    return 1 + contarItensArray(array)

def buscarMaiorItemArray(array, maior_inicial = 0):
    if(array == []):
        return maior_inicial
    
    maior = array.pop(0)

    if(maior > maior_inicial):
        return buscarMaiorItemArray(array, maior)
    else:
        return buscarMaiorItemArray(array, maior_inicial)


# print(fatorial(995))
# print(fatorial_tail(995))

# minha_lista = [0, 45, 5, 80]
# print(somarItensArray(minha_lista))

# minha_lista = list(range(101))
# print(minha_lista)
# print(contarItensArray(minha_lista))

minha_lista = [0, 99, 120, 456, 12, 45000, 78, 99, 987, 125, 653, 753, 159, 1205, 996, 4502, 3598, 7894]
print(buscarMaiorItemArray(minha_lista))