class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
      n = len(word1)
      m = len(word2)
      if n == 0:
        return m
      if m == 0:
        return n
      dp = [[0] * m for _ in range(n)]
      dp[0][0] = 0 if word1[0] == word2[0] else 1
      for i in range(0, m):
        dp[0][i] = i if word1[0] == word2[i] else i + 1
        dp[0][i] = min(dp[0][i - 1] + 1, dp[0][i])
      for i in range(0, n):
        dp[i][0] = i if word1[i] == word2[0] else i + 1
        dp[i][0] = min(dp[i - 1][0] + 1, dp[i][0])
      for i in range(1, n):
        for j in range(1, m):
          need_change = 0 if word1[i] == word2[j] else 1
          dp[i][j] = min(dp[i - 1][j - 1] + need_change, dp[i][j - 1] + 1, dp[i - 1][j] + 1)
      return dp[n - 1][m - 1]
