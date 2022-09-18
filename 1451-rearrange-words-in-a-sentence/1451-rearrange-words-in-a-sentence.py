class Solution:
    def arrangeWords(self, text: str) -> str:
        text = " ".join(sorted(text.lower().split(), key=lambda x: len(x)))
        return text[0].upper() + text[1:]