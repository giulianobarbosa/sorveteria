from reader import get_from_txt
from Digraph import Digraph
from Ordem_Topologica import Ordem_Topologica



if __name__ == "__main__":

    # list_graph = get_from_txt("casos_cohen_t2/casocohen60.txt")
    list_graph = get_from_txt("casos_cohen_t2/casoteste.txt")
    g = Digraph()

    # Adiciona os vértices
    for i in list_graph:
        g.addEdge(i[0], i[1])

    #Cria a ordem topológica
    ot = Ordem_Topologica(g)
    #Listas dos copos
    copos_de_2 = []
    copos_de_3 = []


    for v in ot.pre_order:
        _ = Ordem_Topologica(g, True)
        _.dfs(g, v)
        ls = _.get_pre_order()
        for vi in ls:
            if (v, vi) not in copos_de_2:
                if vi != v:
                    copos_de_2.append((v, vi))
        for vi in ls:
            _2 = Ordem_Topologica(g, True)
            _2.dfs(g, vi)
            ls2 = _2.get_pre_order()
            for vi2 in ls2:
                if (v, vi, vi2) not in copos_de_3:
                    if vi2 != v and vi2 != vi and vi != v:
                        copos_de_3.append((v, vi, vi2))

    print(len(copos_de_2))
    print(len(copos_de_3))