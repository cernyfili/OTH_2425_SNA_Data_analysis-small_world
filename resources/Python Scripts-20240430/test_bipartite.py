import networkx as nx
from networkx.algorithms import bipartite


B = nx.Graph()
B.add_nodes_from([1,2,3,4], bipartite=0) # Add the node attribute "bipartite"
B.add_nodes_from(['a','b','c'], bipartite=1)
B.add_edges_from([(1,'a'), (1,'b'), (2,'b'), (2,'c'), (3,'c'), (4,'a'), (2,'a')])

G = bipartite.projected_graph(B, ['a', 'b','c'], multigraph=True)
print([sorted((u,v)) for u,v in G.edges()])
print (G.edges())  #projection

#weighted projection
G2 = bipartite.weighted_projected_graph(B, ['a', 'b','c'], ratio=False)
print (G2.edges(data=True))  #weighted projection


import matplotlib.pyplot as plt
#draw bipartite network using two colors
pos=nx.spring_layout(B)  

nx.draw(B, pos=pos,node_size = 500, with_labels = True)
nx.draw_networkx_nodes(B, pos, node_color='b',nodelist=[1,2,3,4])
nx.draw_networkx_nodes(B, pos, node_color='yellow',nodelist=['a', 'b','c'])
plt.show()


#draw first projection
nx.draw(G, node_size = 500, node_color="green", with_labels = True)
plt.show()


#draw weighted projection
nx.draw(G2, pos=pos,node_size = 500, with_labels = True)

#consider the weights
all_weights=[]
for (node1,node2,data) in G2.edges(data=True):
	all_weights.append(data['weight']) #we'll use this when determining edge thickness
unique_weights = list(set(all_weights))
#4 c. Plot the edges - one by one!
for weight in unique_weights:
	#4 d. Form a filtered list with just the weight you want to draw
	weighted_edges = [(node1,node2) for (node1,node2,edge_attr) in G2.edges(data=True) if edge_attr['weight']==weight]
	width = weight
	nx.draw_networkx_edges(G2,pos,edgelist=weighted_edges,width=width)
plt.show()
