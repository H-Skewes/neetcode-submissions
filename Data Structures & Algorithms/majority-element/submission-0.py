class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_found = {}
        for i in range(len(nums)):
            if nums[i] not in nums_found:
                nums_found[nums[i]] = 1
            else:
                nums_found[nums[i]] +=1
        highest_key = max(nums_found, key=nums_found.get)
        return highest_key