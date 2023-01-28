estados_abranger = set(['sp', 'rj', 'mg', 'am', 'ce', 'pi', 'mt', 'ms', 'ro', 'go', 'rr'])

estacoes = {}
estacoes["aba"] = set(['sp', 'mg', 'mt'])
estacoes["qwe"] = set(['sp', 'rj', 'ce'])
estacoes["iop"] = set(['mg', 'go', 'ro'])
estacoes["iop"] = set(['mg', 'mt'])
estacoes["fgh"] = set(['ro', 'ce', 'pi'])
estacoes["bnm"] = set(['go', 'rr', 'ms'])
estacoes["tyu"] = set(['rr', 'mg'])
estacoes["jkl"] = set(['am', 'rr'])

estacoes_final = set()

while estados_abranger:
    melhor_estacao = None
    estados_cobertos = set()
    for estacao, estados_por_estacao in estacoes.items():
        cobertos = estados_abranger & estados_por_estacao
        if len(cobertos) > len(estados_cobertos):
            melhor_estacao = estacao
            estados_cobertos = cobertos
            estados_abranger -= estados_cobertos
            estacoes_final.add(melhor_estacao)

print(estacoes_final)