from collections import deque

def hasPath(graph, source, destination):
    stack = deque(source)
    while len(stack)>0:
        current = stack.pop()
        if current==destination:
            return True
        for neighbor in graph[current]:
            stack.append(neighbor)
    return False

graph = {
    'f':['g', 'i'],
    'g':['h'],
    'h':[],
    'i':['g', 'k'],
    'j':['i'],
    'k':[]
}

print(hasPath(graph, 'f', 'k'))