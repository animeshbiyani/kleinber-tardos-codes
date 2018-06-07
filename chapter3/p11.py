from collections import defaultdict

class Graph:
  def __init__(self):
    self.graph = defaultdict(set)
    self.self_edge = defaultdict(list)
    
  def add_edge(self,u,v):
    self.graph[u].add(v)
    self.graph[v].add(u)
    
    c1 = u[0]
    if len(self.self_edge[c1]) == 0:
      self.self_edge[c1].append(u)
    else:
      w = self.self_edge[c1][-1]
      self.graph[w].add(u)
      self.self_edge[c1].append(u)
      
    c2 = v[0]
    if len(self.self_edge[c2]) == 0:
      self.self_edge[c2].append(v)
    else:
      w = self.self_edge[c2][-1]
      self.graph[w].add(v)
      self.self_edge[c2].append(v)
  
  def is_infected(self,c_inf,t_inf,c,t):
    start_node = self.self_edge[c_inf][0]
    explored = defaultdict(lambda : False)
    explored[start_node] = True
    queue = [start_node]
    while queue:
      current_node = queue.pop(0)
      for v in self.graph[current_node]:
        if not explored[v]:
          explored[v] = True
          if v[0] == c and v[1] <= t:
            return True
          queue.append(v)
    return False

g = Graph()
triples = [(1,2,4),(2,4,8),(3,4,8),(1,4,12)]
for c1,c2,t in triples:
  g.add_edge((c1,t),(c2,t))
print(g.is_infected(1,2,3,8))
