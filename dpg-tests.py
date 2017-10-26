import networkx as nx
import math


def dpg_maximum(g: nx.Graph):
    mm = nx.max_weight_matching(g, maxcardinality=True)
    g.remove_edges_from(mm.items())
    g.add_node(nx.number_of_nodes(g))
    for v in mm.keys():
        g.add_edge(v, nx.number_of_nodes(g) - 1)
    return g


data_points = []
G = nx.complete_graph(16)
for i in range(0, 1000):
    data_points.append([len(G), len(nx.max_weight_matching(G, maxcardinality=True)) / 2, nx.density(G),
                        nx.density(nx.Graph.subgraph(G, range(0, math.floor(len(G)/2)))),
                        nx.density(nx.Graph.subgraph(G, range(math.ceil(len(G)/2), len(G))))])
    print(data_points[-1])
    if i > 1:
    #    print(data_points[i][2] - data_points[i - 1][2])
        if data_points[i][1] < data_points[i - 1][1]:
            print(i)

    G = dpg_maximum(G)
