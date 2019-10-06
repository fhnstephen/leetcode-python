class Solution:
    def bestRotation(self, A: List[int]) -> int:
        n = len(A)
        ks = [0 for x in range(n)]
        decs = [0 for x in range(n)]
        for i, x in enumerate(A):
            ks[i] = ((i - x) + n) % n
        for x in ks:
            decs[x] -= 1
        score = 0
        max_ans = 0
        ans = 0
        print(ks)
        print(decs)
        for i in range(1, n):
            score += 1
            score += decs[i - 1]
            if score > max_ans:
                max_ans = score
                ans = i
            print(i, score)
        return ans