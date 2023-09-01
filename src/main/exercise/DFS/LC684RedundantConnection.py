from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # given a graph that started as a tree w/ n nodes labeled: 1 - n
        graph = {}
        for i in range(1,len(edges)+1):
            graph[i] = []

        def dfs(node: int, parent: int) -> bool:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor in visited and parent != neighbor:
                    return True
                if neighbor not in visited:
                    if dfs(neighbor , node):
                        return True

        for u, v in edges:
            visited = set()
            graph[u].append(v)
            graph[v].append(u)

            if dfs(u, v):
                return [u, v]
