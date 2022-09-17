class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        a, b = word, word
        if a[1:].lower() == word[1:]:
            return True
        elif b.upper() == word:
            return True
        else:
            return False
