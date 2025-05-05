import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

matrix = np.array([
    [0, 2, 0, 6],
    [2, 0, 3, 8],
    [0, 3, 0, 0],
    [6, 8, 0, 0]
])

G = nx.from_numpy_array(matrix)

chemin = nx.dijkstra_path(G, source=0, target=2, weight='weight')

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=15)

labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
edges_path = list(zip(chemin[:-1], chemin[1:]))

nx.draw_networkx_edges(G, pos, edgelist=edges_path, edge_color='red', width=3)

plt.title("Graphe Pondéré avec le Chemin de Dijkstra")
plt.show()
