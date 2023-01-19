
def buscarMaiorValorArray(array):
    maiorValor = array[0]
    maior_indice = 0

    for indice in range(1, len(array)):
        if array[indice] > maiorValor:
            maiorValor = array[indice]
            maior_indice = indice

    return maior_indice

def ordenarPorSelecao(array):
    novo_array = []

    for i in range(len(array)):
        menor = buscarMaiorValorArray(array)
        novo_array.append(array.pop(menor))
    return novo_array


minha_lista = [12, 14, 8, 99, 45, -101, 6, 9, 9, 1, 78, 5, -45, 1, 2, 1]
print(ordenarPorSelecao(minha_lista))

