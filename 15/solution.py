class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()
        size = len(nums)
        i = 0
        while i < size - 2:
            first = nums[i]
            if first > 0:
                break
            j = i + 1
            k = size - 1
            while j < k:
                sum = first + nums[j] + nums[k]
                if sum == 0:
                    answer.append((first, nums[j], nums[k]))
                if sum >= 0:
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif sum < 0:
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
            i += 1
            while i < size - 2 and nums[i] == nums[i - 1]:
                i += 1
        return answer
