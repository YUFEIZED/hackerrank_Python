def bfs_path1(graph, a, b):    
    queue = [a]
    visited = {}
    for key in graph:
        visited[key] = False
    visited[a] = True
    step = -1
    while queue:
        vertex = queue.pop(0)
        step +=1
        print(vertex)
        for i in graph[vertex]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
            if i == b:
                print(i)
                step +=1
                return "step is ", step
            
def bfs_path2(graph, a, b):    
    queue = [(a, [a])]
    visited = {}
    for key in graph:
        visited[key] = False
    visited[a] = True
    while queue:
        print(visited)
        (vertex, path) = queue.pop(0)
        print("vertex ", vertex)
        print("path ", path)
        if vertex==b:
            return path
        print("set(path) is ", set(path))
        for i in graph[vertex]:
            if visited[i] == False:
                queue.append((i, path+[i]))
                visited[i] = True
        print("queue is ", queue)
        
def bfs_path3(graph, locationa, locationb):
  queue = [(locationa, [locationa])]
  while queue:
    (vertex, path) = queue.pop(0)
    print("vertex ", vertex)
    print("path ", path)
    if vertex == locationb:
      return path
    print("set(path) is ", set(path))
    for i in graph[vertex] - set(path):
      queue.append((i, path+[i]))
    print("queue is ", queue)
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

path = bfs_path3(graph, a, b)
print(path)
print("steps is ", len(path)-1)
