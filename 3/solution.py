class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        chars = {}
        cur = 0
        left = 0
        for ch in s:
          if ch in chars:
            while s[left] != ch:
              del chars[s[left]]
              left += 1
              cur -= 1
            left += 1
            cur -= 1
          chars[ch] = True
          cur += 1
          if cur > ans:
            ans = cur
        return ans
