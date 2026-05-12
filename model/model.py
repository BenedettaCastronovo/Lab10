import networkx as nx

from database.DAO import DAO


class Model:

    def __init__(self):
        self._grafo = nx.Graph()
        self._mappaN = {}

        #self._nazioni = DAO.getAllNazioni()



    def creaGrafo(self, anno):
        self._grafo.clear()
        self._grafo = nx.Graph()
        self._confini = DAO.getAllConfini(anno)
        self._nazioni = DAO.getAllNazioni(anno)
        for n in self._nazioni:
            self._mappaN[n.CCode] = n
        self._grafo.add_nodes_from(self._nazioni)
        for s in self._confini:
            self._grafo.add_edge(self._mappaN[s.state1no], self._mappaN[s.state2no]) #spacchetto la tupla

    def grado(self):
        diz = {}
        for n in self._grafo.nodes(): #non nella mappa perche potrei avere piu nazioni di quelle nel grafo
            grado = self._grafo.degree[n]

            diz[n.StateNme] = grado
        return diz

    def getNumC(self):
        return nx.number_connected_components(self._grafo)

    def getStati(self):
        return self._grafo.nodes()

    def getCompC(self, source):
        dfsTree = nx.dfs_tree(self._grafo, source)
        lista = list(dfsTree.nodes())
        return lista

        #print("size connessa con dfs_tree", len(dfsTree.nodes()))

        # Strategia 2
        #dfsPred = nx.dfs_predecessors(self._graph, source)
        #print("size connessa con dfs_predecessors", len(dfsPred.values()))

        # Strategia 3
        #conn = nx.node_connected_component(self._graph, source)
        #print("size connessa con node_connected_component", len(conn))