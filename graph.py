import networkx
import matplotlib.pyplot as plt

s = open("out.dolphins", "r", encoding="UTF-8")
lines = s.readlines()

vertices = []
edges = []

for line in lines:
    line = line.strip("\n")
    line = line.split("\t")
    if line[0] != "% sym unweighted":
        if line[0] not in vertices:
            vertices.append(line[0])
    try:
        if line[1] not in vertices:
            vertices.append(line[1])
    except:
        pass
    try:
        if len(line) > 1:
            line = tuple(line)
            edges.append(line)
    except:
        pass

G = nx.Graph()
G.add_nodes_from(vertices)
G.add_edges_from(vertices)

nx.write_gexf(G, "graph.gexf")

pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_color = "red", node_size = 50)
nx.draw_networkx_edges(G, pos, edge_color = "yellow")
plt.axis("off")
plt.show()


