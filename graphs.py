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
    while queue.qsize() > 0:
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

"""
Determine components of G
"""

def determineComponents(G):
    compSet = []
    viableList = set(G.keys())
    for item in G:
        if item in viableList:
            x = is_connected(G, item, set())
            viableList = viableList - x
            compSet.append(x)
    return compSet

"""
Does cycle exist in component specified
"""
def publicDoesCycleExist(G, key):
    return doesCycleExist(G, key, set(), None)

def doesCycleExist(G, key, visitedSet, previousNode):
    visitedSet.add(key)
    for item in G[key]:
        if item not in visitedSet:
            doesCycleExist(G, item, visitedSet, key)
        elif item != previousNode and item in visitedSet:
            return True

    return False
"""
Is the component bipartite
"""
def publicBipartiteComponent(G, key):
    return is_bipartite(G, key, set(), q.Queue())

def is_bipartite(G, key, visitedSet, queue):
    visitedSet.add(key)
    count = 0
    colorDict = {
        #BlUE
        False: set(),
        #RED
        True: set()
    }

    queue.put(key)
    colorDict[count % 2 == 1].add(key)
    count += 1
    while queue.qsize() > 0:
        v = queue.get()
        for item in G[v]:
            if item not in visitedSet:
                queue.put(item)
                visitedSet.add(item)
                colorDict[count % 2 == 1].add(item)
            elif item in colorDict[count % 2 == 0]:
                return False
        count += 1
    return True


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
# print(publicDoesCycleExist(graph, 'J'))
print("Determing if Graph is Bipartite")
print(is_bipartite(graph, 'A', set(), q.Queue()))