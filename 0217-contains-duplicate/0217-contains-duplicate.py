class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        s = 0
        e = s+1
        while e < len(nums):
            if nums[s] == nums[e]:
                s += 1
                e += 1
                return True
            else: 
                s += 1
                e += 1
        return False