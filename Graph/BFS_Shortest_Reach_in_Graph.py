# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 17:15:28 2018

@author: ezyufzh
"""
class Graph:
    def __init__(self, numOfNodes, startNode):
        self.numOfNodes = numOfNodes
        self.startNode = startNode
        self.graphDict = {}
    def createGraph(self, x, y):
        if x not in self.graphDict:
          self.graphDict[x] = set()
        self.graphDict[x].add(y)
        if y not in self.graphDict:
          self.graphDict[y] = set()
        self.graphDict[y].add(x)
        print(self.graphDict)
    def bfs(self, endNode):
        queue = [(self.startNode, [self.startNode])]
        while queue:
            (vertex, path) = queue.pop(0)
            print("vertex ", vertex)
            print("path ", path)
            if vertex == endNode:
                return (len(path)-1)*6
            print("set(path) is ", set(path))
            for i in self.graphDict[vertex] - set(path):
                queue.append((i, path+[i]))
            print("queue is ", queue)     
        return -1
    def findAllDistances(self):
        distance = []
        for i in range(1, self.numOfNodes+1):
            if i != self.startNode:
                distance.append(self.bfs(i))
        return distance
        

n = 4
m = 2
startNode = 1
graph = Graph(n, startNode)
x = 1
y = 2
graph.createGraph(x,y)
x = 1
y = 3
graph.createGraph(x,y)
print(graph.findAllDistances())
