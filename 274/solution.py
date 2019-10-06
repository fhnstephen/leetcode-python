class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        count = [0 for x in range(n + 1)]
        for x in citations:
            count[min(x, n)] += 1
        s = 0
        for x in range(n, -1, -1):
            s += count[x]
            if s >= x:
                return x
    
class Solution1:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        size = len(citations)
        l = 0
        r = size
        ans = 0
        while l + 1 < r:
            mid = (l + r) // 2
            if self.verify(mid, citations):
                l = mid
                if mid > ans:
                    ans = mid
            else:
                r = mid - 1
        if l + 1 > ans and self.verify(l + 1, citations):
            ans = l + 1
        return ans
    
    def verify(self, ans, citations):
        pos = -1
        for i, citation in enumerate(citations):
            if citation >= ans:
                pos = i
                break
            if len(citations) - i < ans:
                break
        if pos != -1 and len(citations) - pos >= ans:
            return True
        return False

