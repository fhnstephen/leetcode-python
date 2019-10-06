class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numTable = {}
        for i, num in enumerate(nums):
            rest = target - num
            if rest in numTable:
                return (numTable[rest], i)
            numTable[num] = i

class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numTable = {}
        for i in range(len(nums)):
            num = nums[i]
            rest = target - num
            if rest in numTable:
                return (numTable[rest], i)
            numTable[num] = i