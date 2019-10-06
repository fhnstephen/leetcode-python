class Solution2:
    def climbStairs(self, n: int) -> int:
        def power(matrix, k, n):
          if k == 1:
            return matrix
          half = power(matrix, k // 2)
          result = mul(half, half, n)
          if k % 2 != 0:
            result = mul(matrix, half, n)
          return result

        def mul(ma, mb, n):
          result = [[0] * n for _ in range(n)]
          for i in range(n):
            for j in range(n):
              for k in range(n):
                result[i][j] += ma[i][k] * mb[k][j]
          return result

        matrix = [[0, 1], [1, 1]]
        result = power(matrix, n - 1, 2)
        if n <= 1:
          return 1
        return result[0][1] + result[1][1]

class Solution:
    def climbStairs(self, n: int) -> int:
        f = [0 for _ in range(n + 1)]
        f[0] = f[1] = 1
        for i in range(2, n + 1):
          f[i] = f[i - 2] + f[i - 1]
        return f[n]
