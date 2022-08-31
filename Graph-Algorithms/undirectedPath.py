edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]

def undirectedPath(edges, source, destination):
    graph = build_graph(edges)
    stack = [source]
    visited = set()
    while len(stack) > 0:
        current = stack.pop()
        if current == destination:
            return True
        for neighbor in graph[current]:
            if neighbor not in visited:
                stack.append(neighbor)
                visited.add(neighbor)

    return False



def build_graph():
    graph = {}
    for edge in edges:
        a, b = edge
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)

    return graph

undirectedPath(edges, 'j', 'm')

