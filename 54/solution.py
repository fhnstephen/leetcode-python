class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        n = len(matrix)
        if n > 0:
          m = len(matrix[0])
        else:
          return ans
        visited = [[False] * m for _ in range(n)]
        cur = (0, 0)
        ans.append(matrix[0][0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d_index = 0
        flag = False
        while True:
          visited[cur[0]][cur[1]] = True
          next = (cur[0] + directions[d_index][0], cur[1] + directions[d_index][1])
          if 0 <= next[0] < n and 0 <= next[1] < m and not visited[next[0]][next[1]]:
            cur = next
            ans.append(matrix[next[0]][next[1]])
            flag = False
          else:
            d_index = (d_index + 1) % 4
            if flag:
              break
            flag = True
        return ans

