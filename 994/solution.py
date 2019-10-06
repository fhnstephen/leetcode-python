class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ans = 0
        q = []
        n = len(grid)
        m = 0
        if n > 0:
            m = len(grid[0])
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == 2:
                    q.append((i, j))
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while len(q) > 0:
            head = q.pop(0)
            for d in dirs:
                new_pos = (head[0] + d[0], head[1] + d[1])
                if new_pos[0] >= 0 and new_pos[0] < n and new_pos[1] >= 0 and new_pos[1] < m and grid[new_pos[0]][new_pos[1]] == 1:
                    q.append(new_pos)
                    grid[new_pos[0]][new_pos[1]] = 2
            ans += 1
            print(q)
            print(grid)
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == 1:
                    return -1
        return ans