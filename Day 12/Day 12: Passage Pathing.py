
class Graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict = []
        self.gdict = gdict
# Add the vertex as a key
    def addVertex(self, vertex):
        if vertex not in self.gdict:
            self.gdict[vertex] = []
# Add edge
    def addEdge(self, edge):
        (vrtx1, vrtx2) = tuple(edge)
        if vrtx1 in self.gdict:
            self.gdict[vrtx1].append(vrtx2)
        else:
            self.gdict[vrtx1] = [vrtx2]
# Find the distinct list of edges
    def getEdges(self):
        edgename = []
        for vrtx in self.gdict:
            for nxtvrtx in self.gdict[vrtx]:
                if {nxtvrtx, vrtx} not in edgename:
                    edgename.append({vrtx, nxtvrtx})
        return edgename

with open("./smallData.txt") as file:
    haha = file.readlines()
nextArr = []
for element in haha:
    nextArr.append(element.strip())
vertexSet = []
for i in range(len(nextArr)):
    skrrt = nextArr[i].split("-")
    for vertex in skrrt:
        if vertex not in vertexSet:
            vertexSet.append(vertex)

graphElements = {}
g = Graph(graphElements)
for node in vertexSet:
    g.addVertex(node)
for edge in nextArr:
    (one, two) = edge.split("-")
    g.addEdge((one, two))
    g.addEdge((two, one))

print(g.getEdges())
print(vertexSet)
print(graphElements)