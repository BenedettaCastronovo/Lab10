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
        for n in self._mappaN:
            grado = self._grafo.degree(self._mappaN[n])

            diz[self._mappaN[n].StateNme] = grado
        return diz

    def getNumC(self):
        return nx.number_connected_components(self._grafo)