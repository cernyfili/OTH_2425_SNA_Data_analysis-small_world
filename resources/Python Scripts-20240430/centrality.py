import collections
import matplotlib.pyplot as plt
import networkx as nx
import operator
import datetime
from time import gmtime, strftime


#Documentation
#https://networkx.github.io/documentation/stable/reference/algorithms/centrality.html

fh=open("zachary.csv", 'rb')
#fh=open("airports.csv", 'rb')
G=nx.read_edgelist(fh,delimiter=',')
fh.close()

print("Number of nodes: ",len(G.nodes))
print("Number of Links: ",len(G.edges))

#degree (in+out)
print("degree_centrality",strftime("%H:%M:%S", gmtime()))
sorted_x = sorted(dict(G.degree()).items(), key=operator.itemgetter(1), reverse=True)
print (sorted_x[:10])

# betweenness_centrality
print("betweenness_centrality",strftime("%H:%M:%S", gmtime()))
Btw = nx.betweenness_centrality(G)
sorted_x = sorted(Btw.items(), key=operator.itemgetter(1), reverse=True)
print (sorted_x[:10])

# edge_betweenness_centrality
print("edge_betweenness_centrality",strftime("%H:%M:%S", gmtime()))
Edg = nx.edge_betweenness_centrality(G)
sorted_x = sorted(Edg.items(), key=operator.itemgetter(1), reverse=True)
print (sorted_x[:10])

# closeness_centrality
print("closeness_centrality",strftime("%H:%M:%S", gmtime()))
Clo = nx.closeness_centrality(G)
sorted_x = sorted(Clo.items(), key=operator.itemgetter(1), reverse=True)
print (sorted_x[:10])

# eigenvector centrality
print("eigenvector_centrality",strftime("%H:%M:%S", gmtime()))
Eig = nx.eigenvector_centrality(G)
sorted_x = sorted(Eig.items(), key=operator.itemgetter(1), reverse=True)
print (sorted_x[:10])

print(strftime("%H:%M:%S", gmtime()))
