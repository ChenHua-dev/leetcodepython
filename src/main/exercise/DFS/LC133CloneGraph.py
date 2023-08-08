from typing import Optional


class Node:
    """
    # Definition for a Node.
    """
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def __init__(self) -> None:
        self.visited = dict()

    def cloneGraph(self, node: Node) -> Optional[Node]:
        if not node:
            return None

        if node in self.visited:
            return self.visited[node]

        node_copy = Node(node.val, [])
        self.visited[node] = node_copy
        for neighbor in node.neighbors:
            neighbor_node = self.cloneGraph(neighbor)
            node_copy.neighbors.append(neighbor_node)

        return node_copy
