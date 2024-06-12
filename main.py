import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

#Load the edge data
edges_data = pd.read_csv('data/edges_test.csv')
print(edges_data.head())

#Load the feature data
features_data = pd.read_csv('data/nodes_test.csv')
print(features_data.head())

G = nx.DiGraph()

for _, row in edges_data.iterrows():
    G.add_edge(row['numeric_id_1'], row['numeric_id_2'])

for _, row in features_data.iterrows():
    node_id = row['numeric_id']
    G.nodes[node_id]['views'] = row['views']
    G.nodes[node_id]['mature'] = row['mature']
    G.nodes[node_id]['life_time'] = row['life_time']
    G.nodes[node_id]['created_at'] = row['created_at']
    G.nodes[node_id]['updated_at'] = row['updated_at']
    G.nodes[node_id]['dead_account'] = row['dead_account']
    G.nodes[node_id]['language'] = row['language']
    G.nodes[node_id]['affiliate'] = row['affiliate']

# Calculate the average clustering coefficient
clustering_coeff = nx.average_clustering(G.to_undirected())
print(f"Average Clustering Coefficient: {clustering_coeff}")

# Average path length

# Ensure the graph is strongly connected
if nx.is_strongly_connected(G):
    avg_path_length = nx.average_shortest_path_length(G)
else:
    # For disconnected graphs, we often use the largest strongly connected component
    largest_scc = max(nx.strongly_connected_components(G), key=len)
    G_largest_scc = G.subgraph(largest_scc)
    avg_path_length = nx.average_shortest_path_length(G_largest_scc)

print(f"Average Path Length: {avg_path_length}")



# Draw the graph
# pos = nx.spring_layout(G)  # positions for all nodes
# nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", edge_color="gray", font_size=10)
# plt.show()