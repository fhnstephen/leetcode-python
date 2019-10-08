class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def dfs(i = 0, j = 0):
          if j == len(p):
            memo[i][j] = i == n
          else:
            if memo[i][j]:
              return memo[i][j]
            first_matched = i < n and p[j] in [s[i], '.']
            if j + 1 < m and p[j + 1] == '*':
              memo[i][j] = first_matched and dfs(i + 1, j) or dfs(i, j + 2)
            else:
              memo[i][j] = first_matched and dfs(i + 1, j + 1)
          return memo[i][j]

        def match(i, j):
          return p[j] == s[i] or p[j] == '.'

        n = len(s)
        m = len(p)
        memo = [[False] * (m + 1) for _ in range(n + 1)]
        return dfs()
