class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        sentence = set(sentence)
        count = 0
        for _ in sentence:
            count += 1
        if count == 26:
            return True
        return False