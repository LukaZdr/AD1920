########## Loesung ##########
def bfs(graph, start):
    visited_nodes = []
    next_nodes = [start]
    while next_nodes != []:
        new_next_nodes = []
        for node in next_nodes:
            if not node in visited_nodes:
                visited_nodes.append(node)
            for child in graph[node]:
                if not child in visited_nodes:
                    new_next_nodes.append(child)
        next_nodes = new_next_nodes
    return visited_nodes

########## Tests ##########

### Test 1
graph = [
    [1,2],
    [0,3,4],
    [0,5],
    [1],
    [1,5],
    [2,4],
]
result = bfs(graph, 0)
print(result)
if result == [0, 1, 2, 3, 4, 5]:
    print("Test 1: Success")
else:
    print("Test 1: Failure")

### Test 2
graph = [
    [1,2],
    [],
    [],
]
result = bfs(graph, 0)
print(result)
if result == [0, 1, 2]:
    print("Test 2: Success")
else:
    print("Test 2: Failure")

### Test 3
graph = [
    [2,1],
    [],
    [],
]
result = bfs(graph, 0)
print(result)
if result == [0, 2, 1]:
    print("Test 3: Success")
else:
    print("Test 3: Failure")