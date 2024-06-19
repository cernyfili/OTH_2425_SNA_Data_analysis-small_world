import matplotlib.pyplot as plt
import networkx as nx
import operator


def random_vaccine(G,n):
	#select n random nodes
	vaccinated=[]
	import random
	while True:
		node = random.randint(0,len(G.nodes())-1)
		if not(node in vaccinated): vaccinated.append(G.nodes()[node])
		if len(vaccinated)==n: return vaccinated

def vaccine_hubs(G,n):
	vaccinated=[]
	sorted_by_degree = sorted(dict(G.degree()).items(), reverse=True, key=operator.itemgetter(1))  
	for j in sorted_by_degree[0:n]:
		vaccinated.append(j[0])
	return vaccinated


def infect_neighbors(G,node,prob):
	import random
	n_list =  [n for n in G.neighbors(node)]
	new_infected=[]
	for j in n_list:
		if random.random()<=prob:
			new_infected.append(j)		
	return new_infected


fh=open("airports.csv", 'rb')
G=nx.read_edgelist(fh,delimiter=',')
fh.close()

#network
G_rand = nx.gnm_random_graph(len(G.nodes()),len(G.edges()))
G_ba = nx.barabasi_albert_graph(len(G.nodes()), 6)
G_sw = nx.watts_strogatz_graph(len(G.nodes()), 6,0.1)
G_sw2 = nx.watts_strogatz_graph(len(G.nodes()), 6,0.3)


Graphs=[G_rand,G_ba,G_sw,G_sw2,G]
Labels=['ER Graph','BA Model','Small World','Small World 2','Airport']
Colors=['r-','y-','g-','p-','c-']

#patient zero
import random
node = random.randint(0,len(G.nodes())-1)


prob = 0.1
prob_recover = 0
steps = 30 # simulation steps

x_axis=[x+1 for x in range(steps)]
fig, ax = plt.subplots()

i=0
for g in Graphs:

	vaccinated=[]
#	vaccinated=random_vaccine(g,100)
	vaccinated=vaccine_hubs(g,300)

	infected=[list(g.nodes())[node]]  #patient zero

	perc_infected=[]
	for j in range(steps):
		new_infected=[]  #new nodes infected in this simulation step
		for k in infected:
			new_infected.extend(infect_neighbors(g,k,prob))

		#can they recover?
		recovered = [x for x in infected if random.random()<=prob_recover]   #nodes recovering these steps
		infected = [x for x in list(set(infected)) if x not in recovered]	 #nodes infected so far = node infected so far minus recovered		
		infected.extend(new_infected)										 #add the nodes infected this step to the list of infected nodes
		infected = [x for x in list(set(infected)) if x not in vaccinated]	 #remove the vaccinated nodes
		perc_infected.append(len(infected)/float(len(g.nodes())))

	plt.plot(x_axis, perc_infected, Colors[i], label=Labels[i])
	i=i+1


# Now add the legend with some customizations.
legend = ax.legend(loc='upper left', shadow=True)


plt.title("Nodes infected")
plt.ylabel("Percentage Nodes infected")
plt.xlabel("Number of Steps")
plt.show()


