from collections import deque

def depthFirstPrint(graph, source):
    print(source)
    for neighbor in graph[source]:
        depthFirstPrint(graph, neighbor)

graph = {
    'a':['b', 'b'],
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