class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)
        f = [[False] * (m + 1) for _ in range(n + 1)]
        if not n:
            return not m or p == '*'
        if not m:
            return not n
        for i in range(m):
            if p[i] == '*':
                if i == 0:
                    f[0][i + 1] = True
                else:
                    f[0][i + 1] = f[0][i]
            else:
                f[0][i + 1] = False
        f[0][0] = True
        for i in range(n):
            for j in range(m):
                matched = p[j] in [s[i], '?']
                cur = matched
                if p[j] == '*':
                    cur = f[i + 1][j] or f[i][j + 1] or f[i][j]
                else:
                    cur = cur and f[i][j]
                f[i + 1][j + 1] = cur
        return f[n][m]
