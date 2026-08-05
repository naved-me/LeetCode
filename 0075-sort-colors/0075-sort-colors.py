from collections import defaultdict
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = defaultdict(int)
        for i in range (len(nums)):
            j = nums[i]
            if j == 0:
                count[0] += 1
            elif j == 1 :
                count[1] += 1
            else:
                count[2] += 1
        nums[:] = [0] * count[0] + [1] * count[1] + [2] * count[2] 
        return nums