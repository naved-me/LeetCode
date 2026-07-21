from collections import deque

class Solution:
    def ladderLength(self, st: str, tar: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if tar not in word_set:
            return 0

        q = deque([(st, 1)])

        while q:
            word, steps = q.popleft()
            if word == tar:
                return steps

            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    newWord = word[:i] + ch + word[i+1:]
                    if newWord in word_set:
                        word_set.remove(newWord)
                        q.append((newWord, steps + 1))

        return 0