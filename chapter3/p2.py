from collections import defaultdict

class Graph:
  def __init__(self,n):
    self.graph = defaultdict(set)
    self.V = n
      
  def add_edge(self,u,v):
    self.graph[u].add(v)
    self.graph[v].add(u)
    
  def add_connections(self,connections):
    for u,v in connections:
      self.add_edge(u,v)
      
  def isCycleUtil(self,u,visited,parent):
    visited[u] = True
    for v in self.graph[u]:
      if not visited[v]:
        if self.isCycleUtil(v,visited,u):
          return True
      elif v != parent:
        return True
    return False
 
  def isCycle(self):
    visited = defaultdict(lambda : False)
    for node in range(self.V):
      if not visited[node]:
        if self.isCycleUtil(node,visited,-1):
          return True
    return False
