def depthFirstPrint(graph, source):
    stack = [source]

    while len(stack) > 0:
        current = stack.pop()
        print(current)
        for neighbor in graph[current]:
            stack.append(neighbor)

graph = {
    'a':['c', 'b'],
    'b':['d'],
    'c':['e'],
    'd':['f'],
    'e':[],
    'f':[]
}

"""
(a)----(c)
 |      |
(b)    (e)
 |
(d)----(f)
ans: a->b->d->f->c-e
"""

depthFirstPrint(graph, 'a')