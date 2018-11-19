def dfs_path(graph, locationa, locationb):
  stack = [(locationa, [locationa])]
  while stack:
    (vertex, path) = stack.pop()
    print("vertex ", vertex)
    print("path ", path)
    if vertex == locationb:
      return path
    print("graph[vertex]", graph[vertex])
    print("set(path) is ", set(path))
    print("graph[vertex] - set(path)", graph[vertex] - set(path))
    for i in graph[vertex] - set(path):
        if i not in [j[0] for j in stack]:
            stack.append((i, path+[i]))
    print("stack is ", stack)
  return -1       
         
graph = {0:set([10,11]),
         1:set([12,9,10]),
         2:set([4]),
         3:set([11,5,6]),
         4:set([8]),
         5:set([3,11]),
         6:set([3]),
         7:set([8,9,11]),
         8:set([12,7]),
         9:set([7,1,11]),
         10:set([1,0]),
         11:set([7,3,5]),
         12:set([1,8])
         }

a = 2
b = 6

path = dfs_path(graph, a, b)
print(path)
print("steps is ", len(path)-1)
