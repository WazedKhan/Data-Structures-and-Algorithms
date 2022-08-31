def connected_components_count(graph):
    visited = set()
    count = 0
    for i in graph:
        if i not in visited:
            count += 1
            stack = [i]
            while len(stack) > 0:
                current = stack.pop()
                for neighbor in graph[current]:
                    if neighbor not in visited:
                        stack.append(neighbor)
                        visited.add(neighbor)
    return count




graph = {
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}

print(connected_components_count(graph))