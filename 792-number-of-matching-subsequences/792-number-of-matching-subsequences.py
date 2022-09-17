class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        count = 0
        d = defaultdict(list)
        for word in words:
            d[word[0]].append(word)
        for char in s:
            temp = d[char]
            d[char] = []
            for word in temp:
                if len(word) == 1:
                    count += 1
                else:
                    d[word[1]].append(word[1:])
        return count
                    