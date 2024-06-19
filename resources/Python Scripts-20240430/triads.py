##############################
# Triangle and Triadic Census
##############################

import networkx as nx

def directed_ER_graph(n,p):
	import random
	G=nx.DiGraph()
	G.add_nodes_from(list(range(1,n+1)))
	for k in range(1,n+1):
		for j in range(1,n+1):
			if random.random()<=p:	G.add_edge(k,j)
	return G




#directed graph
## Run the triadic census
DG = directed_ER_graph(100,0.05)
census = nx.triadic_census(DG)
print (census)


#how to access a dictionary
for key, value in census.items() :
    print (key, value)
