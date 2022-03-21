
import networkx
from matplotlib import pyplot
import numpy as np

# watts-strogatz template.
N = 20      # Number of vertices.
K = 3       # Number of neighbors to connect to.
beta = 0.0  # how is this chosen?

G = networkx.Graph()

for i in range(N):
    G.add_node(i)

# For every node in the loop,
for i in range(N):
    # Connect to its neighbors 
    # N+1,N+2,...N+K (mod N yadda yadda)
    for j in range(K):
        G.add_edge(i, (i+j+1)%N)

# Rewiring step.
edges = list(G.edges)
print(len(edges))
# for every node,
for u in list(G.nodes):
    # find all edges that connect to it.
    neighbors = list(G.neighbors(u))

    ######
    # ALGORITHM FOR "REWIRING":
    # totally at random
    neighbors_plus_me = neighbors + [u]
    others = np.setdiff1d(range(N), neighbors_plus_me)
    others = list(others)
    
    # for each of these edges,
    for v in neighbors:
        # flip a weighted coin; w.p. beta
        # connect to any edge except those 
        # already connected.
        if np.random.rand() < beta:
            vnew = np.random.choice(others)
            others.remove( vnew )
            
            G.remove_edge(u,v)
            G.add_edge(u, vnew)
    #
#

### Visualize
fig,ax = pyplot.subplots(1,1, figsize=(6,6), constrained_layout=True)

networkx.draw_circular(G, ax=ax)

print(len(edges))

fig.show()
