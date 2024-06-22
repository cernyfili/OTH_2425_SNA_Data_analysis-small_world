import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random
import json

# Load the edge data
edges_data = pd.read_csv('data/test/edges_test.csv')  # Replace with your actual path large_twitch_edges7.csv
print("Edges Data:\n", edges_data.head())

# Load the revised feature data
features_data = pd.read_csv('data/test/nodes_test.csv')  # Replace with your actual path large_twitch_features
print("Features Data:\n", features_data.head())


G = nx.DiGraph()

# Add edges to the graph
for _, row in edges_data.iterrows():
    G.add_edge(int(row['numeric_id_1']), int(row['numeric_id_2']))

# Add nodes to the graph and set their attributes
for _, row in features_data.iterrows():
    node_id = int(row['numeric_id'])
    if not G.has_node(node_id):
        G.add_node(node_id)
    G.nodes[node_id]['views'] = int(row['views'])
    G.nodes[node_id]['life_time'] = int(row['life_time'])
    G.nodes[node_id]['created_at'] = row['created_at']
    G.nodes[node_id]['updated_at'] = row['updated_at']
    G.nodes[node_id]['language'] = row['language']

# Descriptive statistics
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
density = nx.density(G)

# Ensure the graph is strongly connected for diameter and avg shortest path
if nx.is_strongly_connected(G):
    diameter = nx.diameter(G)
    avg_shortest_path = nx.average_shortest_path_length(G)
else:
    # For disconnected graphs, use the largest strongly connected component
    largest_scc = max(nx.strongly_connected_components(G), key=len)
    G_largest_scc = G.subgraph(largest_scc).copy()
    diameter = nx.diameter(G_largest_scc)
    avg_shortest_path = nx.average_shortest_path_length(G_largest_scc)

clustering_coefficient = nx.average_clustering(G.to_undirected())
components = nx.number_strongly_connected_components(G)
largest_component = max(nx.strongly_connected_components(G), key=len)
size_largest_component = len(largest_component)
degree_distribution = [int(d) for n, d in G.degree()]

# Print descriptive statistics
print(f"Number of nodes: {num_nodes}")
print(f"Number of edges: {num_edges}")
print(f"Density: {density}")
print(f"Diameter: {diameter}")
print(f"Average shortest path length: {avg_shortest_path}")
print(f"Average clustering coefficient: {clustering_coefficient}")
print(f"Number of strongly connected components: {components}")
print(f"Size of the largest strongly connected component: {size_largest_component}")

# Plot degree distribution
plt.hist(degree_distribution, bins=range(min(degree_distribution), max(degree_distribution) + 1))
plt.title('Degree Distribution')
plt.xlabel('Degree')
plt.ylabel('Frequency')
plt.show()

# Centrality measures
degree_centrality = nx.degree_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)
closeness_centrality = nx.closeness_centrality(G)
pagerank = nx.pagerank(G)

# Print top 5 nodes by degree centrality
top_degree_centrality = sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True)[:5]
print("Top 5 nodes by degree centrality:")
for node, centrality in top_degree_centrality:
    print(f"Node {node}: {centrality}")

# Clustering analysis
clusters = list(nx.community.greedy_modularity_communities(G))
modularity = nx.algorithms.community.quality.modularity(G, clusters)
print(f"Modularity: {modularity}")

# Labeling clusters
for i, cluster in enumerate(clusters):
    print(f"Cluster {i}: {list(cluster)}")

# Resilience analysis: remove random node
node_to_remove = random.choice(list(G.nodes()))
G_removed = G.copy()
G_removed.remove_node(node_to_remove)

new_largest_component = max(nx.strongly_connected_components(G_removed), key=len)
new_size_largest_component = len(new_largest_component)
print(f"Size of the largest component after removing node {node_to_remove}: {new_size_largest_component}")

# Visualization
plt.figure(figsize=(12, 12))
pos = nx.spring_layout(G)
nx.draw_networkx(G, pos, node_size=50, node_color='blue', edge_color='gray')
plt.title('Network Visualization')
plt.show()

# Advanced analysis: Assortativity
assortativity_degree = nx.degree_assortativity_coefficient(G)
print(f"Degree assortativity: {assortativity_degree}")

# Small-world analysis
# Compare with a random graph with the same number of nodes and edges
random_graph = nx.gnm_random_graph(num_nodes, num_edges)
random_clustering_coefficient = nx.average_clustering(random_graph)
largest_cc_random = max(nx.connected_components(random_graph), key=len)
random_shortest_path = nx.average_shortest_path_length(nx.subgraph(random_graph, largest_cc_random))

#print(f"Random graph clustering coefficient: {random_clustering_coefficient}")
#print(f"Random graph average shortest path length: {random_shortest_path}")

# Save results to a file (optional)
results = {
    "num_nodes": int(num_nodes),
    "num_edges": int(num_edges),
    "density": density,
    "diameter": diameter,
    "avg_shortest_path": avg_shortest_path,
    "clustering_coefficient": clustering_coefficient,
    "components": int(components),
    "size_largest_component": size_largest_component,
    "top_degree_centrality": top_degree_centrality,
    "modularity": modularity,
    "assortativity_degree": assortativity_degree,
    "random_clustering_coefficient": random_clustering_coefficient,
    "random_shortest_path": random_shortest_path
}

with open('network_analysis_results.json', 'w') as f:
    json.dump(results, f, indent=4)

print("Analysis complete and results saved to 'network_analysis_results.json'")
