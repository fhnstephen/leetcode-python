class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
      def dfs(x):
        for i in range(numCourses):
          if a[x][i] and ind[i] > 0:
            ind[i] -= 1
            if ind[i] == 0:
              ind[i] = -1
              dfs(i)

      ind = [0 for _ in range(numCourses)]
      a = [[False] * numCourses for _ in range(numCourses)]
      for edge in prerequisites:
        ind[edge[0]] += 1
        a[edge[1]][edge[0]] = True
      for i in range(numCourses):
        if not ind[i]:
          ind[i] = -1
          dfs(i)
      for i in range(numCourses):
        if ind[i] > 0:
          return False
      return True
