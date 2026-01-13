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

cost = {}
cost["Casa"] = 0 #começando de casa 
cost["Marina"] = 5
cost["Pedro"] = 2 #os únicos dois que eu consigo saber começando de casa o percorrimento ou busca 
cost["Luna"] = infinito
cost["Yuri"] = infinito
cost["Icev"] = infinito

parents = {}
parents["Casa"] = None #é a origem, não pode ter pai 
parents["Marina"] = "Casa"
parents["Pedro"] = "Casa"
parents["Luna"] = None
parents["Yuri"] = None
parents["Icev"] = None

processed = []  #no início não tem nenhum processado 

print(graph)