class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        head = 0
        while head < len(nums):
            nums[head] = nums[head]**2
            head += 1
        new_nums = sorted(nums)
        return new_nums