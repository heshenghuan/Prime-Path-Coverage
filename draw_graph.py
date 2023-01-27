import networkx as nx
import matplotlib.pyplot as plt

def draw(graph):
    """Draw the graph and the paths."""
    G = nx.DiGraph()
    # print(graph['nodes'])
    # print(graph['edges'])

    for e in graph['edges']:
        # print(e, graph['edges'][e])
        for n in graph['edges'][e]:
            G.add_edge(e, n)

    color_map = []
    for n in G.nodes():
        # print(n, type(n), type(graph['end']), graph['end'])
        if n==graph['end'][0]:
            color_map.append('red')
        elif n==graph['init'][0]:
            color_map.append('green')
        else:
            color_map.append('lightblue')
    # print('color',color_map)
    # pos = nx.random_layout(G)
    pos = {i: (i%(len(G.nodes())/2), (len(G.nodes())/2) - int(i//(len(G.nodes())/2))) for i in range(len((G.nodes())))}
    # print(pos)
    
    nx.draw(G, pos, with_labels=True, node_color=color_map)
    # nx.draw_networkx_labels(G, pos)
    plt.show()
    # nx.draw_networkx_nodes(G, pos)
    # nx.draw_networkx_edges(G, pos)
    # plt.show()
