# from Ordem_Topologica import Ordem_Topologica

class Digraph:

    def __init__(self):
        self.verts = {}
        self.totalEdges = 0

    def addVert(self, value):
        if value in self.verts:
            return
        self.verts[value] = []


    def addEdge(self, v1, v2):
        if v1 not in self.verts:
            self.addVert(v1)
        if v2 not in self.verts:
            self.addVert(v2)
        assert(v2 not in self.verts[v1])
        self.verts[v1].append(v2)
        self.totalEdges += 1


    def adj(self, v):
        if v not in self.verts:
            return None
        return self.verts[v]
