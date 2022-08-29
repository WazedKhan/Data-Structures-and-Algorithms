from collections import deque

def breadthFirstPrint(graph, source):
    queue = deque(source)
    while len(queue)>0:
        current = queue.popleft()
        print(current)
        for neighbor in graph[current]:
            queue.append(neighbor)

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
breadthFirstPrint(graph, 'a')