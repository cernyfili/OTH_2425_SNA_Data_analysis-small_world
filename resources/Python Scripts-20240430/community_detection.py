#NetworkX 2.1 required!
# upgrade it with: pip install networkx upgrade

import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import community

#G = nx.barbell_graph(5, 1)  #a generated network
#G = nx.path_graph(10)

fh=open("zachary.csv", 'rb')
G=nx.read_edgelist(fh,delimiter=',')
fh.close()


communities = community.girvan_newman(G)

#top level division
top_level_communities = next(communities)
print(top_level_communities)

#second level division
next_level_communities = next(communities)


#Example 2 - show all the divisions (=steps on a dendogram)
print ("Complete steps")
communities = community.girvan_newman(G)

for com in communities:
	print(tuple(sorted(c) for c in com),"\n") 

#compute the modularity of a partition
import networkx.algorithms.community as nx_comm
mod = nx_comm.modularity(G, next_level_communities)

print("Modularity",mod)
mods=[]
communities = community.girvan_newman(G)

for com in communities:
    mods.append(nx_comm.modularity(G, com)) 
    print(nx_comm.modularity(G, com))



#plot modularity
fig, ax = plt.subplots()
cnt = [x for x in range(1,len(mods)+1)]
plt.bar(cnt, mods, width=0.80, color='b')
plt.title("Modularity Histogram")
plt.ylabel("Modularity")
plt.xlabel("Steps")
plt.show()  #show all the figures
				
