grafo = {}
grafo["sjc_inicio"] = {}
grafo["sjc_inicio"]["sao_paulo"] = 90.6
grafo["sjc_inicio"]["rio_de_janeiro"] = 348
#grafo["sjc_inicio"]["belo_horizonte"] = 614

grafo["sao_paulo"] = {}
grafo["sao_paulo"]["curitiba"] = 407
grafo["sao_paulo"]["campinas"] = 93.7
grafo["sao_paulo"]["belo_horizonte"] = 584
grafo["sao_paulo"]["brasilia"] = 1007
#grafo["sao_paulo"]["salvador_fim"] = 1959
grafo["sao_paulo"]["rio_de_janeiro"] = 434

grafo["rio_de_janeiro"] = {}
grafo["rio_de_janeiro"]["sao_paulo"] = 434
grafo["rio_de_janeiro"]["cabo_frio"] = 156
grafo["rio_de_janeiro"]["brasilia"] = 1166
grafo["rio_de_janeiro"]["belo_horizonte"] = 441
#grafo["rio_de_janeiro"]["salvador_fim"] = 1631

grafo["curitiba"] = {}
grafo["curitiba"]["belo_horizonte"] = 1005
grafo["curitiba"]["campinas"] = 479

grafo["campinas"] = {}
grafo["campinas"]["curitiba"] = 479
grafo["campinas"]["cabo_frio"] = 632
grafo["campinas"]["belo_horizonte"] = 578

grafo["belo_horizonte"] = {}
grafo["belo_horizonte"]["campinas"] = 1005
#grafo["belo_horizonte"]["salvador_fim"] = 1349

grafo["brasilia"] = {}
grafo["brasilia"]["belo_horizonte"] = 740
grafo["brasilia"]["salvador_fim"] = 1443

grafo["cabo_frio"] = {}
grafo["cabo_frio"]["campinas"] = 632
grafo["cabo_frio"]["salvador_fim"] = 1608

grafo["salvador_fim"] = {}

infinito = float("inf")
custos = {}
custos["sao_paulo"] = 90.6
custos["rio_de_janeiro"] = 348
custos["curitiba"] = infinito
custos["campinas"] = infinito
custos["belo_horizonte"] = infinito
custos["brasilia"] = infinito
custos["cabo_frio"] = infinito
custos["salvador_fim"] = infinito

pais = {}
pais["sao_paulo"] = "sjc_inicio"
pais["rio_de_janeiro"] = "sjc_inicio"
pais["curitiba"] = None
pais["campinas"] = None
pais["belo_horizonte"] = None
pais["brasilia"] = None
pais["cabo_frio"] = None
pais["salvador_fim"] = None

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
    caminho = ['sjc_inicio']
    ultimo_nodo = caminho[0]

    while ultimo_nodo != 'salvador_fim':
        for nodo in pais.keys():
            if pais[nodo] == ultimo_nodo and nodo not in caminho:
                caminho.append(nodo)
                print(caminho)
                ultimo_nodo = nodo

    return caminho

def buscarMenorCaminhoGrafoRecursivo(cidade_fim):
    if pais.get(cidade_fim) == None:
        return ''

    return buscarMenorCaminhoGrafoRecursivo(pais[cidade_fim]) +' '+ pais[cidade_fim]

def exibirCaminho(cidade_fim):
    return buscarMenorCaminhoGrafoRecursivo(cidade_fim) +' '+ cidade_fim

def exibirDistancia():
    for nodo in custos.keys():
        print(nodo, ': ', custos[nodo])


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
#print(exibeMenorCaminhoGrafo())
exibirDistancia()
print(exibirCaminho('salvador_fim'))
print(exibirCaminho('belo_horizonte'))
print(exibirCaminho('brasilia'))
print(exibirCaminho('curitiba'))
print(exibirCaminho('cabo_frio'))