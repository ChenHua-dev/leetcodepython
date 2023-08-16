from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = {}
        for i in range(n):
            adj_list[i] = []

        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited = set()
        count = 0
        for index in range(n):
            if index not in visited:
                self.dfs(index, edges, visited, adj_list)
                count += 1
        return count

    def dfs(self, index, edges, visited, adj_list):
        if index in visited:
            return
        visited.add(index)
        for neighbor in adj_list[index]:
            self.dfs(neighbor, edges, visited, adj_list)
