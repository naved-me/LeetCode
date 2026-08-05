class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        res = 0
        max_f = 0
        count = {}
        for right in range (len(s)):
            char = s[right]
            if char not in count:
                count[char] = 1
            else:
                count[char] += 1

            if count[char] > max_f:
                max_f = count[char]
            if right - left + 1 - max_f > k:
                count[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res