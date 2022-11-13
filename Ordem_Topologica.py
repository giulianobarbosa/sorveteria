from Digraph import Digraph

class Ordem_Topologica:


    def __init__(self, g:Digraph, c:bool = False):

        self.marked = {i:False for i in g.verts.keys()}
        self.pre_order = []
        if c == False:
            for s in g.verts.keys():
                if self.marked[s] == False:
                    self.dfs(g, s) 


    def dfs(self, g:Digraph, v:str):
        
        self.pre_order.append(v)
        self.marked[v] = True
        if g.adj(v):
            for w in g.adj(v):
                if not self.marked[w]:
                    self.dfs(g, w)

    
    def get_pre_order(self):
        return self.pre_order
