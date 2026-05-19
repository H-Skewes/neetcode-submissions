class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        iterlist = []
        for i in range(0, len(nums)):
            diff = target - nums[i]
            if diff not in iterlist:
                iterlist.insert(i, nums[i])
            else:
                return [iterlist.index(diff), i]
