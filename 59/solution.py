class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = []
        if n == 0:
          return ans
        ans = [[None] * n for _ in range(n)]
        cx = cy = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d_index = 0
        for i in range(n * n):
          ans[cx][cy] = i + 1
          nx, ny = cx + directions[d_index][0], cy + directions[d_index][1]
          if 0 <= nx < n and 0 <= ny < n and ans[nx][ny] is None:
            cx, cy = nx, ny
          else:
            d_index = (d_index + 1) % 4
            cx, cy = cx + directions[d_index][0], cy + directions[d_index][1]
        return ans
