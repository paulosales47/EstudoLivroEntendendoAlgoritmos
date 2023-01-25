from collections import deque
grafo = {} 
grafo["voce"] = ["alice", "bob", "claire"] 
grafo["bob"] = ["anuj", "peggy"]
grafo["alice"] = ["peggy"] 
grafo["claire"] = ["robert", "jonny"]
grafo["robert"] = []
grafo["anuj"] = [] 
grafo["peggy"] = ["antonie", "harry", "tommy"] 
grafo["antonie"] = []
grafo["harry"] = []
grafo["tommy"] = []
grafo["thom"] = ["arthur"]
grafo["arthur"] = []
grafo["jonny"] = ["sofia", "quim"]
grafo["sofia"] = ["voce", "quim"]
#--------------------------------------------------------

def pessoaEVendedor(nome):
    return nome[-1] == 'm'

def buscarVendedorRede(): #PESQUISA EM LARGURA
    fila_de_pesquisa = deque()
    fila_de_pesquisa += grafo["voce"]
    verificados = []

    while fila_de_pesquisa:
        pessoa = fila_de_pesquisa.popleft()
        if not pessoa in verificados:
            if(pessoaEVendedor(pessoa)):
                print(pessoa," é um vendedor")
                return True
            else:
                fila_de_pesquisa += [] if grafo.get(pessoa) == None else grafo[pessoa]
                verificados.append(pessoa)
    return False



print(buscarVendedorRede())

