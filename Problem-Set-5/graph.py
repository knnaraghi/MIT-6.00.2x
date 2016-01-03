# 6.00.2x Problem Set 5
# Graph optimization
#
# A set of data structures to represent graphs
#

class Node(object):
    def __init__(self, name):
        self.name = str(name)
    def getName(self):
        return self.name
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name
    def __eq__(self, other):
        return self.name == other.name
    def __ne__(self, other):
        return not self.__eq__(other)
    def __hash__(self):
        # Override the default hash method
        # Think: Why would we want to do this?
        return self.name.__hash__()

class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return '{0}->{1}'.format(self.src, self.dest)
        
class WeightedEdge(Edge):
    def __init__(self, src, dest, totaldistance, outdoordistance):
        Edge.__init__(self, src, dest)
        self.totaldistance = totaldistance
        self.outdoordistance = outdoordistance
    def getTotalDistance(self):
        return self.totaldistance
    def getOutdoorDistance(self):
        return self.outdoordistance
    def __str__(self):
        return '{0}->{1} ({2}, {3})'.format(self.src, self.dest, self.totaldistance, self.outdoordistance)

class Digraph(object):
    """
    A directed graph
    """
    def __init__(self):
        # A Python Set is basically a list that doesn't allow duplicates.
        # Entries into a set must be hashable (where have we seen this before?)
        # Because it is backed by a hashtable, lookups are O(1) as opposed to the O(n) of a list (nifty!)
        # See http://docs.python.org/2/library/stdtypes.html#set-types-set-frozenset
        self.nodes = set([])
        self.edges = {}
    def addNode(self, node):
        if node in self.nodes:
            # Even though self.nodes is a Set, we want to do this to make sure we
            # don't add a duplicate entry for the same node in the self.edges list.
            raise ValueError('Duplicate node')
        else:
            self.nodes.add(node)
            self.edges[node] = []
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
    def childrenOf(self, node):
        return self.edges[node]
    def hasNode(self, node):
        return node in self.nodes
    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[str(k)]:
                res = '{0}{1}->{2}\n'.format(res, k, d)
        return res[:-1]

class WeightedDigraph(Digraph):
    def __init__(self):
        Digraph.__init__(self)
    def addNode(self, node):
        if node in self.nodes:
            # Even though self.nodes is a Set, we want to do this to make sure we
            # don't add a duplicate entry for the same node in the self.edges list.
            raise ValueError('Duplicate node')
        else:
            self.nodes.add(node)
            self.edges[node] = []
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append([dest, (edge.getTotalDistance(), edge.getOutdoorDistance())])
    def childrenOf(self, node):
        #return [i for i, _ in self.edges[node]]
        children = []
        for x in self.edges[node]:
            #node is an object so must iterate over elements and retrieve only the destination node and exclude distances
            children.append(x[0])
        return children
    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[k]:
                #d is dictionary elements - d[0] is is the destination node and d[1] represents the totaldistance and outdoordistance
                totaldistance, outdoordistance = d[1]
                res = '{0}{1}->{2} ({3}, {4})\n'.format(res, k, d[0], float(totaldistance), float(outdoordistance))
        return res[:-1]

#g = WeightedDigraph()
#na = Node('a')
#nb = Node('b')
#nc = Node('c')
#g.addNode(na)
#g.addNode(nb)
#g.addNode(nc)
#e1 = WeightedEdge(na, nb, 15, 10)
#print e1
#print e1.getTotalDistance()
#print e1.getOutdoorDistance()
#e2 = WeightedEdge(na, nc, 14, 6)
#e3 = WeightedEdge(nb, nc, 3, 1)
#print e2
#print e3
#g.addEdge(e1)
#g.addEdge(e2)
#g.addEdge(e3)
#print g

#nh = Node('h')
#nj = Node('j')
#nk = Node('k')
#nm = Node('m')
#ng = Node('g')
#g = WeightedDigraph()
#g.addNode(nh)
#g.addNode(nj)
#g.addNode(nk)
#g.addNode(nm)
#g.addNode(ng)
#randomEdge = WeightedEdge(nj, nm, 91, 59)
#g.addEdge(randomEdge)
#randomEdge = WeightedEdge(nm, nj, 40, 31)
#g.addEdge(randomEdge)
#randomEdge = WeightedEdge(nm, nk, 33, 29)
#g.addEdge(randomEdge)
#randomEdge = WeightedEdge(nj, nm, 17, 15)
#g.addEdge(randomEdge)
#randomEdge = WeightedEdge(nk, nh, 52, 8)
#g.addEdge(randomEdge)
#randomEdge = WeightedEdge(nh, nm, 91, 22)
#g.addEdge(randomEdge)
#randomEdge = WeightedEdge(nk, nm, 70, 67)
#g.addEdge(randomEdge)
#randomEdge = WeightedEdge(nk, nh, 72, 18)
#g.addEdge(randomEdge)
#print g.childrenOf(nh) 
#print g.childrenOf(nj) 
#print g.childrenOf(nk) 
#print g.childrenOf(nm) 
#print g.childrenOf(ng) 
