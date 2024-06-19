import collections
import matplotlib.pyplot as plt
import networkx as nx
import numpy
import powerlaw


fh=open("airports.csv", 'rb')
G=nx.read_edgelist(fh,delimiter=',')
fh.close()
G = nx.barabasi_albert_graph(10000,10)



degree_sequence=sorted([d for d in dict(G.degree()).values()], reverse=True) # degree sequence sorted from the highest one

degreeCount=collections.Counter(degree_sequence)
print (degreeCount.items())
deg, cnt = zip(*degreeCount.items())

data = cnt
results = powerlaw.Fit(data)
print("alpha", results.power_law.alpha)
print("xmin",results.power_law.xmin)
print("signma",results.power_law.sigma)

powerlaw.plot_pdf(data, color="b")

R, p = results.distribution_compare('power_law', 'lognormal')
print(R,p)

R, p = results.distribution_compare('power_law', 'exponential')
print(R,p)