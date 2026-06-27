class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [0] * n 
        head = 0
        tail = n - 1
        insert = n - 1 
        while head <= tail:
            if abs(nums[head]) > abs(nums[tail]):
                res[insert] = nums[head] ** 2
                head += 1
            else:
                res[insert] = nums[tail] ** 2
                tail -= 1
            insert -= 1
        return res