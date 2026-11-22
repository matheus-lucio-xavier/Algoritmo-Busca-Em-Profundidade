vertices = ["v1", "v2", "v3", "v4", "v5", "v6", "v7", "v8"]
arestas = [
    ["v1", "v2"],
    ["v1", "v3"],
    ["v1", "v6"],
    ["v2", "v1"],
    ["v2", "v3"],
    ["v2", "v4"],
    ["v2", "v6"],
    ["v2", "v7"],
    ["v3", "v1"],
    ["v3", "v2"],
    ["v4", "v2"],
    ["v4", "v5"],
    ["v5", "v4"],
    ["v5", "v6"],
    ["v5", "v8"],
    ["v6", "v1"],
    ["v6", "v2"],
    ["v6", "v5"],
    ["v6", "v7"],
    ["v7", "v2"],
    ["v7", "v6"],
    ["v7", "v8"],
    ["v8", "v5"],
    ["v8", "v7"]
]

def vizinhos(arestas, vertice):
    vizinhos = []
    
    for _origem, _destino in arestas:
        if _origem == vertice:
            vizinhos.append(_destino)

    return vizinhos

# Busca padra de profundidade que recebe valor inicial e retorna lista de visitados em ordem que foram visitados
def busca_padrao(arestas, inicio):
    visitados = []
    pilha = [inicio]

    while pilha:
        visitados.append(pilha[-1])
        for vizinho in vizinhos(arestas, pilha[-1]):
            if vizinho not in pilha and vizinho not in visitados:
                pilha.append(vizinho)
        
        pilha.pop(-1)

    return visitados

# Busca por ciclos retorna um bool se houver um ciclo partindo do vertice inicial
def busca_por_ciclos(arestas, inicio):
    visitados = []
    pilha = [
        {
            'vertice': inicio,
            'pai': None
        }
    ]

    while pilha:
        visitados.append(pilha[-1]['vertice'])
        for vizinho in vizinhos(arestas, pilha[-1]['vertice']):
            if vizinho not in pilha and vizinho not in visitados:
                pilha.append(
                    {
                        'vertice': vizinho,
                        'pai': pilha[-1]['vertice']
                    })
            else:
                if vizinho != pilha[-1]['pai']:
                    return True
        
        pilha.pop(-1)

    return False

def __main__():
    print("## Algoritmo de Busca em Profundidade ##")
    print("Vertices registrados: ")
    print(vertices)
    inicio = input("Digite por qual vertice deseja iniciar: ")

    print("Vertices visitados em ordem de busca: ")
    print(busca_padrao(arestas, inicio))

    print(f"Há um ciclo partindo do vertice digitado?: {"Sim" if busca_por_ciclos(arestas, inicio) else "Não"}")

__main__()