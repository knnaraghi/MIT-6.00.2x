# 6.00.2x Problem Set 5
# Graph optimization
# Finding shortest paths through MIT buildings
#

import string
# This imports everything from `graph.py` as if it was defined in this file!
from graph import * 

#
# Problem 2: Building up the Campus Map
#
# Before you write any code, write a couple of sentences here 
# describing how you will model this problem as a graph. 

# This is a helpful exercise to help you organize your
# thoughts before you tackle a big design problem!
#

def load_map(mapFilename):
    """ 
    Parses the map file and constructs a directed graph

    Parameters: 
        mapFilename : name of the map file

    Assumes:
        Each entry in the map file consists of the following four positive 
        integers, separated by a blank space:
            From To TotalDistance DistanceOutdoors
        e.g.
            32 76 54 23
        This entry would become an edge from 32 to 76.

    Returns:
        a directed graph representing the map
    """
    #initalize WeightedDigraph class
    graph = WeightedDigraph()
    #set of nodes that we will add to
    nodes = graph.nodes
    #open filename and read only
    mitmap = open(mapFilename, 'r')
    #parse thru each line in file
    for line in mitmap:
        params = line.split()
        src = Node(params[0])
        dest = Node(params[1])
        totaldistance = float(params[2])
        outdoordistance = float(params[3])
        #if src not in nodes:
            #nodes.append(src)
        #using try-except blocks because addNode function will raise value error if duplicate
        try:
            graph.addNode(src)
        except:
            pass
        try:
            graph.addNode(dest)
        except:
            pass
        #if dest not in nodes:
            #nodes.append(dest)
        edge = WeightedEdge(src, dest, totaldistance, outdoordistance)
        graph.addEdge(edge)
    return graph
    print "Loading map from file..."
        
#mitMap = load_map("mit_map.txt") # change to proper directory
#print isinstance(mitMap, WeightedDigraph)
#print mitMap.nodes
#print mitMap.edges
#
# Problem 3: Finding the Shortest Path using Brute Force Search
#
# State the optimization problem as a function to minimize
# and what the constraints are
#

def bruteForceSearch(digraph, start, end, maxTotalDist, maxDistOutdoors):    
    """
    Finds the shortest path from start to end using brute-force approach.
    The total distance travelled on the path must not exceed maxTotalDist, and
    the distance spent outdoor on this path must not exceed maxDistOutdoors.

    Parameters: 
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by 
        a list of building numbers (in strings), [n_1, n_2, ..., n_k], 
        where there exists an edge from n_i to n_(i+1) in digraph, 
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
    
    path = getValidPaths(digraph, start, end, path = [], valid_paths = [])
    shortest  = getShortestPath(digraph, maxTotalDist, maxDistOutdoors, path)
    if shortest == None:
       raise ValueError
    else:
        return shortest

def getValidPaths(digraph, start, end, path = [], valid_paths = []):
    path = path + [start]
    if start == end:
        valid_paths.append(path)
    for node in digraph.childrenOf(Node(start)):
        if str(node) not in path: #avoid cycles
            getValidPaths(digraph, str(node), end, path, valid_paths)
    return valid_paths
    
def dfsBestPath(digraph, start, end, maxTotalDist, maxDistOutdoors, path = [], best = None):
    path = path + [start]
    if start == end:
        return path
    for node in digraph.childrenOf(Node(start)):
        if str(node) not in path: #avoid cycles
            current_path = dfsBestPath(digraph, str(node), end, maxTotalDist, maxDistOutdoors, path, best)
            #path = []
            if current_path != None:
                total_distance, outdoor_distance = getDistance(digraph, current_path)
                if total_distance <= maxTotalDist and outdoor_distance <= maxDistOutdoors:
                    best = current_path
                    maxTotalDist = total_distance
    
    return best

def getShortestPath(digraph, maxTotalDist, maxDistOutdoors, valid_paths):
    shortest_distance = maxTotalDist
    shortest_path = []
    for path in valid_paths:
        total = 0.0
        outdoor = 0.0
        for node in range(len(path)-1):
            edges = digraph.edges[Node(path[node])]
            for edge in edges:
                if str(edge[0]) == path[node +1]:
                    total += float(edge[1][0])
                    outdoor += float(edge[1][1])
        if total <= shortest_distance and outdoor <= maxDistOutdoors:
            shortest_path = path
            shortest_distance = total
    if len(shortest_path) == 0:
        raise ValueError
    
    return shortest_path

def getDistance(digraph, path): 
    "digraph is a graph and path is a list of strings"
    total = 0.0
    outdoor = 0.0
    for node in range(len(path)-1):
        edges = digraph.edges[Node(path[node])]
        for edge in edges:
            if str(edge[0]) == path[node +1]:
                total += float(edge[1][0])
                outdoor += float(edge[1][1])
    
    return total, outdoor
    
      
#
# Problem 4: Finding the Shorest Path using Optimized Search Method
#
def directedDFS(digraph, start, end, maxTotalDist, maxDistOutdoors):
    """
    Finds the shortest path from start to end using directed depth-first.
    search approach. The total distance travelled on the path must not
    exceed maxTotalDist, and the distance spent outdoor on this path must
	not exceed maxDistOutdoors.

    Parameters: 
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by 
        a list of building numbers (in strings), [n_1, n_2, ..., n_k], 
        where there exists an edge from n_i to n_(i+1) in digraph, 
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
    best = dfsBestPath(digraph, start, end, maxTotalDist, maxDistOutdoors, path = [], best = None)
    if best == None:
       raise ValueError
    else:
        return best

# Uncomment below when ready to test
#### NOTE! These tests may take a few minutes to run!! ####
if __name__ == '__main__':
#     Test cases
     mitMap = load_map("mit_map.txt") # change to proper directory
     print isinstance(mitMap, Digraph)
     print isinstance(mitMap, WeightedDigraph)
     print 'nodes', mitMap.nodes
     print 'edges', mitMap.edges


     LARGE_DIST = 1000000

#     Test case 1
     print "---------------"
     print "Test case 1:"
     print "Find the shortest-path from Building 32 to 56"
     expectedPath1 = ['32', '56']
     brutePath1 = bruteForceSearch(mitMap, '32', '56', LARGE_DIST, LARGE_DIST)
     dfsPath1 = directedDFS(mitMap, '32', '56', LARGE_DIST, LARGE_DIST)
     print "Expected: ", expectedPath1
     print "Brute-force: ", brutePath1
     print "DFS: ", dfsPath1
     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath1 == brutePath1, expectedPath1 == dfsPath1)

#     Test case 2
     print "---------------"
     print "Test case 2:"
     print "Find the shortest-path from Building 32 to 56 without going outdoors"
     expectedPath2 = ['32', '36', '26', '16', '56']
     brutePath2 = bruteForceSearch(mitMap, '32', '56', LARGE_DIST, 0)
     dfsPath2 = directedDFS(mitMap, '32', '56', LARGE_DIST, 0)
     print "Expected: ", expectedPath2
     print "Brute-force: ", brutePath2
     print "DFS: ", dfsPath2
     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath2 == brutePath2, expectedPath2 == dfsPath2)

#     Test case 3
     print "---------------"
     print "Test case 3:"
     print "Find the shortest-path from Building 2 to 9"
     expectedPath3 = ['2', '3', '7', '9']
     brutePath3 = bruteForceSearch(mitMap, '2', '9', LARGE_DIST, LARGE_DIST)
     dfsPath3 = directedDFS(mitMap, '2', '9', LARGE_DIST, LARGE_DIST)
     print "Expected: ", expectedPath3
     print "Brute-force: ", brutePath3
     print "DFS: ", dfsPath3
     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath3 == brutePath3, expectedPath3 == dfsPath3)

#     Test case 4
     print "---------------"
     print "Test case 4:"
     print "Find the shortest-path from Building 2 to 9 without going outdoors"
     expectedPath4 = ['2', '4', '10', '13', '9']
     brutePath4 = bruteForceSearch(mitMap, '2', '9', LARGE_DIST, 0)
     dfsPath4 = directedDFS(mitMap, '2', '9', LARGE_DIST, 0)
     print "Expected: ", expectedPath4
     print "Brute-force: ", brutePath4
     print "DFS: ", dfsPath4
     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath4 == brutePath4, expectedPath4 == dfsPath4)

#     Test case 5
     print "---------------"
     print "Test case 5:"
     print "Find the shortest-path from Building 1 to 32"
     expectedPath5 = ['1', '4', '12', '32']
     brutePath5 = bruteForceSearch(mitMap, '1', '32', LARGE_DIST, LARGE_DIST)
     dfsPath5 = directedDFS(mitMap, '1', '32', LARGE_DIST, LARGE_DIST)
     print "Expected: ", expectedPath5
     print "Brute-force: ", brutePath5
     print "DFS: ", dfsPath5
     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath5 == brutePath5, expectedPath5 == dfsPath5)

#     Test case 6
     print "---------------"
     print "Test case 6:"
     print "Find the shortest-path from Building 1 to 32 without going outdoors"
     expectedPath6 = ['1', '3', '10', '4', '12', '24', '34', '36', '32']
     brutePath6 = bruteForceSearch(mitMap, '1', '32', LARGE_DIST, 0)
     dfsPath6 = directedDFS(mitMap, '1', '32', LARGE_DIST, 0)
     print "Expected: ", expectedPath6
     print "Brute-force: ", brutePath6
     print "DFS: ", dfsPath6
     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath6 == brutePath6, expectedPath6 == dfsPath6)

#     Test case 7
     print "---------------"
     print "Test case 7:"
     print "Find the shortest-path from Building 8 to 50 without going outdoors"
     bruteRaisedErr = 'No'
     dfsRaisedErr = 'No'
     try:
         bruteForceSearch(mitMap, '8', '50', LARGE_DIST, 0)
     except ValueError:
         bruteRaisedErr = 'Yes'
    
     try:
         directedDFS(mitMap, '8', '50', LARGE_DIST, 0)
     except ValueError:
         dfsRaisedErr = 'Yes'
    
     print "Expected: No such path! Should throw a value error."
     print "Did brute force search raise an error?", bruteRaisedErr
     print "Did DFS search raise an error?", dfsRaisedErr

#     Test case 8
     print "---------------"
     print "Test case 8:"
     print "Find the shortest-path from Building 10 to 32 without walking"
     print "more than 100 meters in total"
     bruteRaisedErr = 'No'
     dfsRaisedErr = 'No'
     try:
         bruteForceSearch(mitMap, '10', '32', 100, LARGE_DIST)
     except ValueError:
         bruteRaisedErr = 'Yes'
    
     try:
         directedDFS(mitMap, '10', '32', 100, LARGE_DIST)
     except ValueError:
         dfsRaisedErr = 'Yes'
    
     print "Expected: No such path! Should throw a value error."
     print "Did brute force search raise an error?", bruteRaisedErr
     print "Did DFS search raise an error?", dfsRaisedErr
