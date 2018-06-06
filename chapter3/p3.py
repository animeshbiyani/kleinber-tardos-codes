from collections import defaultdict,Counter

class Graph:
  def __init__(self,numVertices):
    self.graph = defaultdict(set)
    self.V = numVertices
    
  def add_edge(self,u,v):
    self.graph[u].add(v)
    
  def add_connections(self,connections):
    for u,v in connections:
      self.add_edge(u,v)
      
  def print_cycle_util(self,u,visited,T):
    visited[u] = True
    T.append(u)
    for v in self.graph[u]:
      if not visited[v]:
        self.print_cycle_util(v,visited,T)
      
  def print_cycle(self,u):
    T = []
    visited = defaultdict(lambda : False)
    visited[u] = True
    
    for v in self.graph[u]:
      if not visited[v]:
        T.append(u)
        self.print_cycle_util(v,visited,T)
    return T
      
  def is_dag(self):
    in_degree = Counter()
    for nodes in self.graph.values():
      for node in nodes:
        in_degree[node] += 1
        
    S = [node for node in range(self.V) if in_degree[node] == 0]
    top_order = []
    
    while S:
      node = S.pop(0)
      top_order.append(node)
      
      for n in self.graph[node]:
        in_degree[n] -= 1
        if in_degree[n] == 0:
          S.append(n)
          
    if len(top_order) != self.V:
      print("The graph is not a DAG, it contains the following cycle")
    else:
      print("The graph is a DAG, and its topological ordering is")
      return top_order
