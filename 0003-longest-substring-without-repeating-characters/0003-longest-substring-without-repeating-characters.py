class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        start = 0
        max_length = 0
        for end in range(len(s)):
            # While the incoming character is ALREADY in our set,
            # shrink the window from the left!
            while s[end] in char_set:
                char_set.remove(s[start])
                start += 1 
            # Add the new character and update max length
            char_set.add(s[end])
            max_length = max(max_length, end - start + 1)
        return max_length