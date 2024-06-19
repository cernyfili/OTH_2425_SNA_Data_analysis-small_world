import pandas as pd
import networkx as nx
from matplotlib import pyplot as plt
import community


def print_top5_degree(graph):
    # Calculate the degree centrality for each node
    degree_centrality = nx.degree_centrality(graph)
    # Sort nodes by their degree centrality in descending order
    sorted_nodes = sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True)
    # Print the top 5 nodes based on degree centrality
    print("Top 5 Nodes based on Degree Centrality:")
    for node, centrality in sorted_nodes[:5]:
        print(f"{node}: {centrality}")

# top5 on betweenes centrality
def print_top5_betweenness(graph):
    # Calculate the betweenness centrality for each node
    betweenness_centrality = nx.betweenness_centrality(graph)
    # Sort nodes by their betweenness centrality in descending order
    sorted_nodes = sorted(betweenness_centrality.items(), key=lambda x: x[1], reverse=True)
    # Print the top 5 nodes based on betweenness centrality
    print("Top 5 Nodes based on Betweenness Centrality:")
    for node, centrality in sorted_nodes[:5]:
        print(f"{node}: {centrality}")

# top5 on closeness centrality
def print_top5_closeness(graph):
    # Calculate the closeness centrality for each node
    closeness_centrality = nx.closeness_centrality(graph)
    # Sort nodes by their closeness centrality in descending order
    sorted_nodes = sorted(closeness_centrality.items(), key=lambda x: x[1], reverse=True)
    # Print the top 5 nodes based on closeness centrality
    print("Top 5 Nodes based on Closeness Centrality:")
    for node, centrality in sorted_nodes[:5]:
        print(f"{node}: {centrality}")

# average shortest path length
def print_avg_shortest_path_length(graph):
    # Calculate the average shortest path length
    avg_shortest_path_length = nx.average_shortest_path_length(graph)
    print(f"Average Shortest Path Length: {avg_shortest_path_length}")

#  size of the giant component
def print_giant_component_size(graph):
    # Get the giant component of the graph
    giant_component = max(nx.connected_components(graph), key=len)
    # Calculate the size of the giant component
    giant_component_size = len(giant_component)
    print(f"Size of the Giant Component: {giant_component_size}")

# number of components
def print_number_of_components(graph):
    # Calculate the number of connected components in the graph
    num_components = nx.number_connected_components(graph)
    print(f"Number of Components: {num_components}")

# isolated nodes
def print_isolated_nodes(graph):
    # Find the isolated nodes in the graph
    isolated_nodes = list(nx.isolates(graph))
    print(f"Isolated Nodes: {isolated_nodes}")

#average cluster coe�icient
def print_avg_cluster_coefficient(graph):
    # Calculate the average clustering coefficient
    avg_cluster_coefficient = nx.average_clustering(graph)
    print(f"Average Clustering Coefficient: {avg_cluster_coefficient}")

# Find average shortest path (if the network is not fully connected, you need to first
# extract the giant component)
def print_avg_shortest_path_length(graph):
    # Get the giant component of the graph
    giant_component = max(nx.connected_components(graph), key=len)
    # Calculate the average shortest path length
    avg_shortest_path_length = nx.average_shortest_path_length(graph.subgraph(giant_component))
    print(f"Average Shortest Path Length: {avg_shortest_path_length}")

# Plot the degree distribution
def plot_degree_distribution(graph):
    degrees = [graph.degree(node) for node in graph.nodes()]
    plt.hist(degrees, bins=20, color='skyblue', edgecolor='black')
    plt.xlabel('Degree')
    plt.ylabel('Frequency')
    plt.title('Degree Distribution')
    plt.show()

# Find the best community split (maximizing modularity)
def find_best_community_split(graph):
    # Find the best community split using the Louvain method
    best_partition = nx.community.louvain_communities(graph, seed=123)
    # Calculate the modularity of the best community split
    modularity = nx.community.modularity(graph, best_partition)
    print(f"Modularity: {modularity}")
    print("Community Partition:", best_partition)
    return best_partition

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('data/wolrd_countries_net.csv')

# Create a directed graph
G = nx.from_pandas_edgelist(df, source='Country_A', target='Country_B')

print_top5_degree(G)
print_top5_betweenness(G)
print_top5_closeness(G)
print_avg_shortest_path_length(G)
print_giant_component_size(G)
print_number_of_components(G)
print_isolated_nodes(G)
print_avg_cluster_coefficient(G)
print_avg_shortest_path_length(G)
plot_degree_distribution(G)
find_best_community_split(G)
