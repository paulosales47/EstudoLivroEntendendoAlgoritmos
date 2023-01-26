grafo = {}
grafo["inicio"] = {}
grafo["inicio"]["a"] = 6
grafo["inicio"]["b"] = 2

grafo["a"] = {}
grafo["a"]["fim"] = 1

grafo["b"] = {}
grafo["b"]["a"] = 3
grafo["b"]["fim"] = 5

grafo["fim"] = {}

infinito = float("inf")
custos = {}
custos["a"] = 6
custos["b"] = 2
custos["fim"] = infinito

pais = {}
pais["a"] = "inicio"
pais["b"] = "inicio"
pais["fim"] = None

nodos_processados = []

def procurarVerticeMenorCusto():
    custo_mais_baixo = float("inf")
    nodo_custo_mais_baixo = None

    for nodo in custos:
        custo = custos[nodo]
        if custo < custo_mais_baixo and nodo not in nodos_processados:
            custo_mais_baixo = custo
            nodo_custo_mais_baixo = nodo
    return nodo_custo_mais_baixo

def buscarCaminhoMenorCusto():
    nodo = procurarVerticeMenorCusto()
    
    while nodo is not None:
        custo = custos[nodo]
        vizinhos = grafo[nodo]
        for n in vizinhos.keys():
            novo_custo = custo + vizinhos[n]
            if custos[n] > novo_custo:
                custos[n] = novo_custo
                pais[n] = nodo
        nodos_processados.append(nodo)
        nodo = procurarVerticeMenorCusto()


def exibeMenorCaminhoGrafo():
    caminho = ['inicio']
    ultimo_nodo = caminho[0]

    while ultimo_nodo != 'fim':
        for nodo in pais.keys():
            if pais[nodo] == ultimo_nodo and nodo not in caminho:
                caminho.append(nodo)
                ultimo_nodo = nodo

    return caminho

# print('--------------------------')
# print('ANTES')
# print('--------------------------')
# print(grafo.keys())
# print('--------------------------')
# print(pais.keys())
# print(pais.values())
# print('--------------------------')
# print(custos.keys())
# print(custos.values())
buscarCaminhoMenorCusto()
# print('--------------------------')
# print('DEPOIS')
# print('--------------------------')
# print(grafo.keys())
# print('--------------------------')
# print(pais.keys())
# print(pais.values())
# print('--------------------------')
# print(custos.keys())
# print(custos.values())
print(exibeMenorCaminhoGrafo())
print(pais.get('inicio'))