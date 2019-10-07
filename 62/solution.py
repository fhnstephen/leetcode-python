from queue import Queue
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        f = [[0] * m for _ in range(n)]
        f[0][0] = 1
        dx = [0, 1]
        dy = [1, 0]
        q = Queue()
        q.put((0, 0))
        visited = [[False] * m for _ in range(n)]
        while not q.empty():
          head = q.get()
          x, y = head
          for i in range(2):
            nx, ny = x + dx[i], y + dy[i]
            if nx < n and ny < m:
              if not visited[nx][ny]:
                q.put((nx, ny))
                visited[nx][ny] = True
              f[nx][ny] += f[x][y]
        return f[n - 1][m - 1]

