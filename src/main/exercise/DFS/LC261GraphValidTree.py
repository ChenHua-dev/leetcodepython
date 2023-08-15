from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) + 1 != n:
            return False

        dag = [[] for _ in range(n)]
        for i, j in edges:
            dag[i].append(j)
            dag[j].append(i)

        seen = set()

        def dfs(cur):
            if cur in seen:
                return
            seen.add(cur)
            for adj in dag[cur]:
                dfs(adj)

        dfs(0)
        return len(seen) == n
