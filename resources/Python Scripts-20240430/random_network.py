"""
Generate a random graph
Draw degree histogram with matplotlib.
Add a box to the histogram with some network stats: average degree, size of the giant component, average cluster coefficient
"""
import collections
import matplotlib.pyplot as plt
import networkx as nx

#a function to get the average of a list
def avg(l):   
	return sum(l) / float(len(l))
 

	
G = nx.gnp_random_graph(1000, 0.02)  #generate a random graph, 100 nodes, p=0.02 (probabilituy of a link)

degree_sequence=sorted([d for d in dict(G.degree()).values()], reverse=True) # degree sequence sorted from the highest one

degreeCount=collections.Counter(degree_sequence)
deg, cnt = zip(*degreeCount.items())  #cnt are the value of the degree


#Find the Connected compoments
CC = sorted(nx.connected_components(G), key = len, reverse=True) #sort by len, the first element is the giant component
gcc = len(CC[0])/float(len(G.nodes()))   #compute the size of the giant component over the total number of nodes
print ("% of Giant Component: ", gcc)

#culster coefficient
avg_cf = nx.average_clustering(G)


fig, ax = plt.subplots()
plt.bar(deg, cnt, width=0.80, color='b')

plt.title("Degree Histogram")
plt.ylabel("Count")
plt.xlabel("Degree")
ax.set_xticks([d+0.4 for d in deg])
ax.set_xticklabels(deg)


#prepare the textbox
textstr = '<d>=%.2f\nGCC=%.2f\n<cf>=%.2f'%(avg(degree_sequence), 100*gcc, avg_cf)

# these are matplotlib.patch.Patch properties for the label
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

# place a text box in upper left in axes coords
ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=13,
        verticalalignment='top', bbox=props)


plt.show()  #show all the figures

#plot shortest path of network of different sizes
#keep the degree constant to verify it
# since degree = (n-1)*p, set the probability to  p = degree / (n-1) to get always a constant degree

sizes = [x for x in range(25,1500,25)]
path_rnd = []
degree = 20
for s in sizes:
    print("Network size",s)
    G = nx.gnp_random_graph(s, degree/(s-1))  #generate a random graph, 100 nodes, p=0.1 (probabilituy of a link)
    path_rnd.append(nx.average_shortest_path_length(G))

#plot average shortest path
fig, ax = plt.subplots()
plt.title("Average Shortest Path")
plt.ylabel("Average shortest path")
plt.xlabel("Network Size")
plt.plot([d for d in sizes],path_rnd)

plt.show()  #show all the figures
