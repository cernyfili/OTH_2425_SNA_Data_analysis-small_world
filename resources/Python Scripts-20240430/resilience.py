import matplotlib.pyplot as plt
import networkx as nx
import operator
#from datetime import datetime
#import collections

def avg(l):
	return sum(l)/len(l)


def sizeGCC(G):
    CC = sorted(nx.connected_components(G), key = len, reverse=True) #sort by len, the first element is the giant component
    gcc = len(CC[0])/float(len(G.nodes()))   #compute the size of the giant component over the total number of nodes
    return gcc

def remove_nodes(G,n,node_list):
	for j in node_list[0:n]:
		G.remove_node(j[0])
	return G

def remove_random_nodes(G,n):
	import random
	for j in range(n):
		node = random.randint(0,len(G.nodes())-1)
		G.remove_node(list(G.nodes())[node])
	return G



#Create two copies of the airports network
fh=open("airports.csv", 'rb')
G=nx.read_edgelist(fh,delimiter=',')
fh.close()

fh=open("airports.csv", 'rb')
G2=nx.read_edgelist(fh,delimiter=',')
fh.close()

#random network
G_rand = nx.gnm_random_graph(len(G.nodes()),len(G.edges()))

#Small World network
avg_degree = int(len(G.edges()) / len(G.nodes()))
print(avg_degree)
SWN = nx.watts_strogatz_graph(len(G.nodes()), avg_degree, 0.1, seed=None)
#Lattice
#Lattice=nx.grid_graph(dim=[50,50]) 
BA = nx.barabasi_albert_graph(3000, 5, seed=None)


#Connected compoments
CC = sorted(nx.connected_components(SWN), key = len, reverse=True) #sort by len, the first element is the giant component
gcc = len(CC[0])/float(len(SWN.nodes()))



deg=[]  #x axis

tgt = []
rnd=[]
er=[]
sw=[]
ba_n=[]

path_tgt = []
path_rnd = []
path_er = []

num_nodes= 20 # remove 20 nodes each time
for j in range(100):
	print("Removing...",j*num_nodes,"nodes...")
	deg.append(j*num_nodes)
	#add the value of the GCC to each serie
	tgt.append(sizeGCC(G))
	rnd.append(sizeGCC(G2))
	er.append(sizeGCC(G_rand))
	sw.append(sizeGCC(SWN))
	ba_n.append(sizeGCC(BA))
	
#	path_tgt.append(nx.average_shortest_path_length(max(nx.connected_component_subgraphs(G), key=len)))
#	path_rnd.append(nx.average_shortest_path_length(max(nx.connected_component_subgraphs(G2), key=len)))
#	path_er.append(nx.average_shortest_path_length(max(nx.connected_component_subgraphs(G_rand), key=len)))

	remove_random_nodes(G2,num_nodes)  #random failure on airports
	
	#targeted attack on airports
	sorted_by_degree = sorted(dict(G.degree()).items(), reverse=True, key=operator.itemgetter(1))  
	remove_nodes(G,num_nodes,sorted_by_degree)
	
	#targeted attack on random network
	sorted_by_degree = sorted(dict(G_rand.degree()).items(), reverse=True, key=operator.itemgetter(1))
	remove_nodes(G_rand,num_nodes,sorted_by_degree)

	#targeted attack on small world network
	sorted_by_degree = sorted(dict(SWN.degree()).items(), reverse=True, key=operator.itemgetter(1))
	remove_nodes(SWN,num_nodes,sorted_by_degree)

	#targeted attack on small BA network
	sorted_by_degree = sorted(dict(BA.degree()).items(), reverse=True, key=operator.itemgetter(1))
	remove_nodes(BA,num_nodes,sorted_by_degree)


fig, ax = plt.subplots()
plt.plot(deg, tgt, 'b-', label="Targeted")
plt.plot(deg, rnd,'r-', label="Failure")
plt.plot(deg, er,'y-', label="Failure (Random Graph)")
plt.plot(deg, sw,'g-', label="Targeted (Small World)")
plt.plot(deg, ba_n,'c-', label="Targeted (Barabasi)")

# Now add the legend with some customizations.
legend = ax.legend(loc='lower left', shadow=True)


plt.title("Size of the GCC")
plt.ylabel("Size (%)")
plt.xlabel("Number of Nodes Removed")
plt.show()

#shortest path graph
'''
fig, ax = plt.subplots()
plt.plot(deg, path_tgt, 'b-', label="Targeted")
plt.plot(deg, path_rnd,'r-', label="Failure")
plt.plot(deg, path_er,'y-', label="Failure (Random Graph)")

# Now add the legend with some customizations.
legend = ax.legend(loc='lower left', shadow=True)


plt.title("Avg. shortest Path")
plt.ylabel("Steps")
plt.xlabel("Number of Nodes Removed")
plt.show()


'''
