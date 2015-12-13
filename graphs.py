import Queue as q

"""
Note to reader: the public methods exist because Python doesn't allow method overloading
"""

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E']),
         'G': set(['X', 'Y']),
         'X': set(['G', 'Z']),
         'Y': set(['G']),
         'Z': set(['X']),
         'J': set(['K']),
         'K': set(['J'])}

"""
DEPTH-FIRST SEARCH
"""
def publicDFS(G, key):
    DFS(G, key, set())    

def DFS(G, key, visitedSet):
    print(key)
    visitedSet.add(key)
    for item in G[key]:
        if item not in visitedSet:
            DFS(G, item, visitedSet)
    # Print call can alternatively be here

"""
BREADTH-FIRST SEARCH
"""
def publicBFS(G, key):
    BFS(G, key, set(), q.Queue())

def BFS(G, key, visitedSet, queue):
    visitedSet.add(key)
    queue.put(key)
    while queue.qsize > 0:
        v = queue.get()
        print v
        for item in G[v]:
            if item not in visitedSet:
                queue.put(item)
                visitedSet.add(item)

"""
CONNECTIVITY
"""
def publicIs_connected(G, v, w):
    x = is_connected(G, v, set())
    return w in x

def is_connected(G, key, visitedSet):
    visitedSet.add(key)
    for item in G[key]:
        if item not in visitedSet:
            is_connected(G, item, visitedSet)
    return visitedSet

def determineComponents(G):
    compSet = []
    viableList = set(G.keys())
    for item in G:
        if item in viableList:
            x = is_connected(G, item, set())
            viableList = viableList - x
            compSet.append(x)
    return compSet

def publicDoesCycleExist(G, key):
    print(doesCycleExist(G, key, set(), None))

def doesCycleExist(G, key, visitedSet, previousNode):
    visitedSet.add(key)
    for item in G[key]:
        if item not in visitedSet:
            doesCycleExist(G, item, visitedSet, key)
        elif item != previousNode and item in visitedSet:
            return True

    return False

# print("DFS WITH C AS ROOT")
# publicDFS(graph, 'C')
# print("BFS WITH C AS ROOT")
# publicBFS(graph, 'C')
# print ("Connectivity test")
# print(publicIs_connected(graph, 'C', 'G'))
# print(publicIs_connected(graph, 'B', 'C'))
# print(publicIs_connected(graph, 'Z', 'G'))
# print("Determining Components")
# print(determineComponents(graph))
publicDoesCycleExist(graph, 'J')