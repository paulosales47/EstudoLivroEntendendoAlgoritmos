import math

def pesquisa_binaria(lista, item):
    baixo = 0;
    alto = len(lista) - 1;
    
    if(item > lista[alto]):
        return None;

    while baixo <= alto:
        meio = math.ceil((baixo + alto) / 2);
        chute = lista[meio];
        print('chute: ', chute);
        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1;
        else:
            baixo = meio + 1
    return None

minha_lista = list(range(0,8192))
print(pesquisa_binaria(minha_lista, 1023))





