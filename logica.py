#implentando um exemplo de percorrimento de graph na menor distância possivel 
infinito = float("inf")

#criando o graph ja com a distância entre os nós 
graph = {}
graph["Casa"] = {}
graph["Casa"]["Marina"] = 5
graph["Casa"]["Pedro"] = 2
graph["Marina"] = {}
graph["Marina"]["Luna"] = 15
graph["Marina"]["Yuri"] = 10
graph["Pedro"] = {}
graph["Pedro"]["Luna"] = 20
graph["Pedro"]["Yuri"] = 35
graph["Luna"] = {}
graph["Luna"]["Icev"] = 5
graph["Yuri"] = {}
graph["Yuri"]["Icev"] = 5
graph["Icev"] = {}

costs = {}
costs["Casa"] = 0 #começando de casa 
costs["Marina"] = 5
costs["Pedro"] = 2 #os únicos dois que eu consigo saber começando de casa o percorrimento ou busca 
costs["Luna"] = infinito
costs["Yuri"] = infinito
costs["Icev"] = infinito

parents = {}
parents["Casa"] = None #é a origem, não pode ter pai 
parents["Marina"] = "Casa"
parents["Pedro"] = "Casa"
parents["Luna"] = None
parents["Yuri"] = None
parents["Icev"] = None

processed = []  #no início não tem nenhum processado 

print(graph) 

def no_mais_barato(costs):
    custo_mais_barto = infinito
    no_mais_barato = None
    for no in costs:
        cost = costs[no]
        if cost < custo_mais_barto and no not in processed:
            custo_mais_barto = cost
            no_mais_barato = no
    return no_mais_barato    


destiny = "Icev"
no = no_mais_barato(costs)
while no is not None:
    cost = costs[no]
    vizinhos = graph[no]
    for n in vizinhos.keys():
        new_cost = cost + vizinhos[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = no
    processed.append(no)
    no = no_mais_barato(costs)


def print_way(parents, destiny):
    way = []
    current = destiny
    while current is not None:
        way.append(current)
        current = parents.get(current)  #forma de evitar um KeyErro 
    if way[-1] == "Casa":   #Se o último for CASA, significa que o caminho é valido(significa que a ordem da fila é feita de como se fosse voltando do caminho final à partida)
        way.reverse()
        return " -> ".join(way)
    else:
        return f"Nenhum caminho encontrado até o destino {destiny}"

#print(graph)
print(costs)
print(parents)

caminho = print_way(parents, destiny)
print("O melhor caminho até o nó ", destiny, ":", caminho)    
    