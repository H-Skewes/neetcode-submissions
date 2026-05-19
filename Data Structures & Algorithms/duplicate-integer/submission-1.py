class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        moreThanOnce = False
        nums.sort()
        for n in range(len(nums)-1):
            if nums[n] == nums[n+1]:
                moreThanOnce = True
        return moreThanOnce