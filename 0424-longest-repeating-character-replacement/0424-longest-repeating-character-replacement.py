class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        window_count = {} # consider a freq map 
        res = 0

        for right in range(len(s)):
            window_count[s[right]] = window_count.get(s[right], 0) + 1
            # while current wondow size - maxFreq > k remove left element and move left by one index
            while (right - left + 1) - max(window_count.values()) > k:
                window_count[s[left]] -= 1
                left += 1
            # compute max window size    
            res = max(right - left + 1, res)
        return res