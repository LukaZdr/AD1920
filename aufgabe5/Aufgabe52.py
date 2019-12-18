########## Loesung ##########
def dfs(graph, start):
    return dsf_rekursive(graph, start, [])

def dsf_rekursive(graph, start, visited):
    visited.append(start)
    children = graph[start]
    for child in children:
        if not child in visited:
            dsf_rekursive(graph, child, visited)
    return visited

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
result = dfs(graph, 0)
if result == [0, 1, 3, 4, 5, 2]:
    print("Test 1: Success")
else:
    print("Test 1: Failure")

### Test 2
graph = [
    [1,2],
    [],
    [],
]
result = dfs(graph, 0)
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
result = dfs(graph, 0)
if result == [0, 2, 1]:
    print("Test 3: Success")
else:
    print("Test 3: Failure")