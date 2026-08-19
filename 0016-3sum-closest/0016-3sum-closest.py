class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        
        # Initialize with the sum of the first three elements
        closest_sum = nums[0] + nums[1] + nums[2]
        
        for i in range(n - 2):
            l = i + 1
            r = n - 1
            
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                
                if total == target:
                    return total  # Found exact match, return immediately
                
                # If this new total is closer to the target, update our best guess
                if abs(total - target) < abs(closest_sum - target):
                    closest_sum = total
                
                # Move pointers based on how the total compares to the target
                if total < target:
                    l += 1
                else:
                    r -= 1
                    
        return closest_sum
