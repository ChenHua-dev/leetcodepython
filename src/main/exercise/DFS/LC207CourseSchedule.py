from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # map each course to a prereq list
        adj_list = {}
        for i in range(numCourses):
            adj_list[i] = []

        for lst in prerequisites:
            course = lst[0]
            prereq = lst[1]
            adj_list[course].append(prereq)

        # visited set
        visited = set()
        for c in range(numCourses):
            if not self.dfs(c, visited, adj_list):
                return False
        return True

    def dfs(self, course, visited, adj_list) -> bool:
        if course in visited:
            return False
        if adj_list[course] == []:
            return True
        visited.add(course)
        for prereq in adj_list[course]:
            if not self.dfs(prereq, visited, adj_list):
                return False
        visited.remove(course)
        adj_list[course] = []
        return True
    
