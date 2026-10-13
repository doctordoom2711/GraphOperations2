def count_sink_nodes(graph, start):
    visited = set()
    stack = [start]
    sink_count = 0

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            if not graph.get(node):
                sink_count += 1
            for neighbor in graph.get(node, list()):
                if neighbor not in visited:
                    stack.append(neighbor)
    return sink_count

if __name__ == "__main__":
    g = {
        0: list(),
        1: list(),
        2: list(),
        3: list(),
        4: list()
    }
    print(count_sink_nodes(g, 0))
