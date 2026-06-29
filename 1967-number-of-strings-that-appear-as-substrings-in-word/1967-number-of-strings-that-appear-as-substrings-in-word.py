class Solution:
    def numOfStrings(self, patterns: list[str], word: str) -> int:
        count = 0
        
        # Loop through each string in the patterns array
        for pattern in patterns:
            # The 'in' keyword handles the substring search automatically
            if pattern in word:
                count += 1
                
        return count