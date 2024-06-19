import collections
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

#define function to calculate Gini coefficient
def gini(x):
    total = 0
    for i, xi in enumerate(x[:-1], 1):
        total += np.sum(np.abs(xi - x[i:]))
    return total / (len(x)**2 * np.mean(x))

def avg(l):
	return sum(l)/len(l)
	


#### Use the airport network (remove comments)
#fh=open("zachary.csv", 'rb')
#fh=open("airports_last.csv", 'rb')
fh=open("euro_roads.csv", 'rb')
G=nx.read_edgelist(fh,delimiter=',')
fh.close()

### Use a random network with same nodes and avg. degree as the
### airport network
#p=10.37/3440   #probability of a link = avg. degree / # of nodes
#G = nx.gnp_random_graph(3440, p)

### Use small world network model
#G = nx.watts_strogatz_graph(len(G.nodes()), 5, 0.1, seed=None)


degree_sequence=sorted([d for d in dict(G.degree()).values()], reverse=True) # degree sequence sorted from the highest one

degreeCount=collections.Counter(degree_sequence)
#print the distribution
print (degreeCount.items())
deg, cnt = zip(*degreeCount.items())  #cnt are the value of the degree


fig, ax = plt.subplots()
plt.bar(deg, cnt, width=0.80, color='b')

#Connected compoments
CC = sorted(nx.connected_components(G), key = len, reverse=True) #sort by len, the first element is the giant component
gcc = len(CC[0])/float(len(G.nodes()))

plt.title("Degree Histogram")
plt.ylabel("Count")
plt.xlabel("Degree")
ax.set_xticks([d+0.4 for d in deg])
ax.set_xticklabels(deg)

textstr = '<d>=%.2f\nGCC=%.2f\nGini=%.2f'%(avg(degree_sequence), 100*gcc,gini(np.array(degree_sequence)))

# these are matplotlib.patch.Patch properties for the label
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=13,
        verticalalignment='top', bbox=props)

plt.show()  #show all the figures
				
