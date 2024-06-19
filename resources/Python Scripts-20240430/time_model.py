import networkx as nx
import collections
import matplotlib.pyplot as plt

#a function to get the average of a list
def avg(l):   
	return sum(l) / float(len(l))


def pick_random(n,node_list):
	#pick n random number from a list
	import random
	picks=[]
	while True:
		num = random.randint(0,len(node_list)-1)
		if num not in picks: picks.append(num)
		if len(picks)==n: return picks


n_start = 15  #initial  number of nodes
m = 10 #number of edges for each new nodes
n = 10000 # final size of the network

G=nx.complete_graph(n_start)


for j in range(n_start,n):
	picks=pick_random(m,G.nodes())
	G.add_node(j)
	for l in picks: G.add_edge(j,l)
	print (j)

#export to gephi
nx.write_gexf(G, "time_model.gexf")

degree_sequence=sorted([d for d in dict(G.degree()).values()], reverse=True)  #take the degree of each node and sort them from the highest one
degreeCount=collections.Counter(degree_sequence)  #generate a frequency distribution, a list of pairs (degree,count), telling you for each degree the number of nodes with that degree
deg, cnt = zip(*degreeCount.items())
print("TM",degree_sequence[1:10])

fig, ax = plt.subplots()		#generate a plot with a figure and an axis object
plt.bar(deg, cnt, width=0.80, color='b')	#draw the histogram

#set some features of the graph
plt.title("Degree Histogram")
plt.ylabel("Count")
plt.xlabel("Degree")
ax.set_xticks([d+0.4 for d in deg])
ax.set_xticklabels(deg)


#Find the Connected compoments
CC = sorted(nx.connected_components(G), key = len, reverse=True) #sort by len, the first element is the giant component
gcc = len(CC[0])/float(len(G.nodes()))   #compute the size of the giant component over the total number of nodes

#culster coefficient
avg_cf = nx.average_clustering(G)

#prepare the textbox
textstr = '<d>=%.2f\nGCC=%.2f\n<cf>=%.2f'%(avg(degree_sequence), 100*gcc, avg_cf)

# these are matplotlib.patch.Patch properties for the label
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

# place a text box in upper left in axes coords
ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=13,
        verticalalignment='top', bbox=props)


plt.show()  #show all the figures

G = nx.dense_gnm_random_graph(10000,10000*10)

degree_sequence=sorted([d for d in dict(G.degree()).values()], reverse=True)  #take the degree of each node and sort them from the highest one
degreeCount=collections.Counter(degree_sequence)  #generate a frequency distribution, a list of pairs (degree,count), telling you for each degree the number of nodes with that degree
deg, cnt = zip(*degreeCount.items())
print("ER",degree_sequence[1:10])

fig, ax = plt.subplots()		#generate a plot with a figure and an axis object
plt.bar(deg, cnt, width=0.80, color='b')	#draw the histogram

#set some features of the graph
plt.title("Degree Histogram")
plt.ylabel("Count")
plt.xlabel("Degree")
ax.set_xticks([d+0.4 for d in deg])
ax.set_xticklabels(deg)


#Find the Connected compoments
CC = sorted(nx.connected_components(G), key = len, reverse=True) #sort by len, the first element is the giant component
gcc = len(CC[0])/float(len(G.nodes()))   #compute the size of the giant component over the total number of nodes

#culster coefficient
avg_cf = nx.average_clustering(G)

#prepare the textbox
textstr = '<d>=%.2f\nGCC=%.2f\n<cf>=%.2f'%(avg(degree_sequence), 100*gcc, avg_cf)

# these are matplotlib.patch.Patch properties for the label
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

# place a text box in upper left in axes coords
ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=13,
        verticalalignment='top', bbox=props)


plt.show()  #show all the figures

G = nx.barabasi_albert_graph(10000,10)

degree_sequence=sorted([d for d in dict(G.degree()).values()], reverse=True)  #take the degree of each node and sort them from the highest one
degreeCount=collections.Counter(degree_sequence)  #generate a frequency distribution, a list of pairs (degree,count), telling you for each degree the number of nodes with that degree
deg, cnt = zip(*degreeCount.items())
print("BA",degree_sequence[1:10])
fig, ax = plt.subplots()		#generate a plot with a figure and an axis object
plt.bar(deg, cnt, width=0.80, color='b')	#draw the histogram

#set some features of the graph
plt.title("Degree Histogram")
plt.ylabel("Count")
plt.xlabel("Degree")
ax.set_xticks([d+0.4 for d in deg])
ax.set_xticklabels(deg)


#Find the Connected compoments
CC = sorted(nx.connected_components(G), key = len, reverse=True) #sort by len, the first element is the giant component
gcc = len(CC[0])/float(len(G.nodes()))   #compute the size of the giant component over the total number of nodes

#culster coefficient
avg_cf = nx.average_clustering(G)

#prepare the textbox
textstr = '<d>=%.2f\nGCC=%.2f\n<cf>=%.2f'%(avg(degree_sequence), 100*gcc, avg_cf)

# these are matplotlib.patch.Patch properties for the label
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

# place a text box in upper left in axes coords
ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=13,
        verticalalignment='top', bbox=props)


plt.show()  #show all the figures