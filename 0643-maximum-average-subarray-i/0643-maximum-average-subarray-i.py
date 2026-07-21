class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        # Step 1: Compute the sum of the very first window of size k
        current_sum = sum(nums[:k])
        max_sum = current_sum
        
        # Step 2: Slide the window from index k to the end of the array
        for i in range(k, len(nums)):
            # Subtract the element leaving the left, add the element entering the right
            current_sum += nums[i] - nums[i - k]
            
            # Keep track of the highest sum seen so far
            max_sum = max(max_sum, current_sum)
            
        # Step 3: Divide by k to return the maximum average
        return max_sum / k