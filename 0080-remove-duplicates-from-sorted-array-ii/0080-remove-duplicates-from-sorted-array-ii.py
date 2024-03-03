class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        placeIdx = 2
        for rightIdx in range(2, len(nums)):
            visitedNum = nums[rightIdx]
            if  visitedNum !=  nums[placeIdx - 2]:
                nums[placeIdx] = visitedNum
                placeIdx  += 1
        return placeIdx