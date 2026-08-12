from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = defaultdict(int)
        left , res = 0, 0
        for right in range (len(fruits)):
            count[fruits[right]] += 1
            if len(count) > 2 :
                count[fruits[left]] -= 1
                if count[fruits[left]]==0:
                    del count[fruits[left]]
                left += 1
            res = max(res,right-left+1)
        return res