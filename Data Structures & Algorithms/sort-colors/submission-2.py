class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lowbound = 0
        currel = 0
        highbound = len(nums)-1
        while currel <= highbound:
            if nums[currel] == 0:
                nums[lowbound], nums[currel] = nums[currel], nums[lowbound]
                lowbound += 1
                currel += 1
            elif nums[currel] == 1:
                currel +=1
            else:
                nums[currel], nums[highbound] = nums[highbound], nums[currel]
                highbound -= 1