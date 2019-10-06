class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Manacher Algorithm
        s = '#' + '#'.join(s) + '#'
        pos = 0
        max_right = 0
        ans = ""
        size = len(s)
        rl = [1 for x in range(size)]
        for i in range(size):
            if i <= max_right:
                rl[i] = min(rl[pos * 2 - i], max_right - i)
            while i - rl[i] >= 0 and i + rl[i] < size and s[i - rl[i]] == s[i + rl[i]]:
                rl[i] += 1
            if i + rl[i] - 1 > max_right:
                max_right = i + rl[i] - 1
                pos = i
            if rl[i] - 1 > len(ans):
                ans = s[i - rl[i] + 1:i + rl[i] - 1].replace('#', '')
        return ans

class Solution2:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if size == 0:
            return ""
        ans = 1
        ans_str = s[0]
        f = [[0 for x in range(size)] for y in range(size)]
        for i in range(size):
            f[i][i] = True
            if i + 1 < size and s[i] == s[i + 1]:
                f[i][i + 1] = True
                f[i + 1][i] = True
                ans = 2
                ans_str = s[i: i + 2]
        for k in range(3, size + 1):
            if k > ans + 2:
                break
            for i in range(size - k + 1):
                j = i + k - 1
                f[i][j] = f[i + 1][j - 1] and s[i] == s[j]
                if f[i][j] and k > ans:
                    ans = k
                    ans_str = s[i:j + 1]
        return ans_str

class Solution1:
    def longestPalindrome(self, s: str) -> str:
        ans = 0
        ans_str = ""
        size = len(s)
        for i in range(len(s)):
            j = i
            k = i
            while j >= 0 and k < size and s[j] == s[k]:
                if k - j + 1 > ans:
                    ans = k - j + 1
                    ans_str = s[j:k + 1]
                j -= 1
                k += 1
        for i in range(len(s)):
            j = i
            k = i + 1
            while j >= 0 and k < size and s[j] == s[k]:
                if k - j + 1 > ans:
                    ans = k - j + 1
                    ans_str = s[j:k + 1]
                j -= 1
                k += 1
        return ans_str